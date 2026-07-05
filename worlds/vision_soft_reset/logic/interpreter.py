from types import FunctionType, MethodType
from collections import UserString
import sys
from pathlib import Path
from functools import reduce
from typing import Any, Callable
from enum import Enum

class ParseState(Enum):
    NEXT = 0
    CALL = 1
    QUOTE = 2
    TOKEN = 3
    STRING_LITERAL = 4
    STRING_LITERAL_ESCAPE = 5
    COMMENT = 6

class TokenType(Enum):
    NORMAL = 0
    SYMBOL = 1
    LITERAL = 2
    NUMERIC = 3
    STRING = 4

class LispSymbol(str):
    def __str__(self) -> str:
        return "'" + self

class LispLiteral(str):
    def __str__(self) -> str:
        return ":" + self

class StackFrame:
    def __init__(self, name: str, pos: tuple[int, int], f: Path,
                 vars: dict[str, Any],
                 funcs: dict[str, tuple[Callable, str, str | None]]):
        self.name = name
        self.args: list[Any] = []
        self.pos = pos
        self.argpos: list[tuple[int, int]] = []
        self.f = f
        self.vars: dict[str, Any] = vars.copy()
        self.funcs: dict[str, tuple[Callable, str, str | None]] = funcs.copy()

    def arg(self, value: Any, pos: tuple[int, int]):
        self.args.append(value)
        self.argpos.append(pos)

    def __repr__(self) -> str:
        return f"<Stack frame {self.name} at {self.pos} in {self.f}>"

def func_info(func, name: str | None = None, sig: str | None = None, doc: str | None = None) -> tuple[str, Callable, str, str | None]:
    if sig is None:
        if isinstance(func, FunctionType) or isinstance(func, MethodType):
            fc = func.__code__
            args = fc.co_varnames[0:fc.co_argcount]
            if isinstance(func, MethodType):
                args = args[1:] # strip out self
            sig = reduce(lambda a, b: a + ' ' + str(b), args, '').lstrip()
        else:
            raise TypeError(f"Cannot infer function signature for builtin function {func.__name__}!")
    if doc is None:
        doc = func.__doc__
    if name is None:
        name = func.__name__
    # print(name, sig, doc)
    return (name, func, sig, doc)

def list_of(*items: Any) -> list[Any]:
    return list(items)

class LispState:
    global_vars: dict[str, Any] = {}
    global_funcs: dict[str, tuple[Callable, str, str | None]] = {}

    @staticmethod
    def set_global(name: str, value: Any):
        LispState.global_vars[name] = value

    @staticmethod
    def register_global(func: Callable, name: str | None = None, sig: str | None = None, doc: str | None = None):
        info = func_info(func, name, sig, doc)
        LispState.global_funcs[info[0]] = info[1:]

    @staticmethod
    def reset():
        LispState.global_vars = {}
        LispState.global_funcs = {}

    @staticmethod
    def dump_defs(filename):
        with open(filename, "w") as f:
            f.write(";;; Generated lisp definitions for python functions\n")
            for name in LispState.global_funcs:
                func_data = LispState.global_funcs[name]
                f.write("\n")
                f.write(f"({name}")
                if len(func_data[1]) > 0:
                    f.write(f" ({func_data[1]})")
                if func_data[2] is not None:
                    f.write(f"\n  \"{func_data[2]}\"")
                f.write(")\n")

    def __init__(self, path: Path):
        path = path.resolve()
        self.base_path = path.parent
        self.paths: list[Path] = [path]
        self.current_path = path
        self.stack: list[StackFrame] = []

        self.set_global("nil", None)
        self.set_global("true", True)
        self.set_global("false", False)

        self.register_global(self.require)
        self.register_global(self.set_lisp, "set")
        self.register_global(self.set_many, "set*", "[sym value]...")
        self.register_global(print, "print", "args...")
        self.register_global(list_of, "list", "args...")

        # print(f"init lisp env at {self.base_path}")
        self.stack.append(StackFrame("<toplevel>", (0, 0), self.current_path, LispState.global_vars, LispState.global_funcs))

    def push_file(self, path: Path):
        path = path.resolve()
        if not path.is_relative_to(self.base_path):
            raise ValueError("Attempted to require file above directory of root file!")
        self.paths.append(path)
        self.current_path = path
        self.push_frame("<toplevel>", (0, 0))

    def pop_file(self):
        self.paths.pop()
        self.stack.pop()
        if len(self.paths) > 0:
            self.current_path = self.paths[-1]
        else:
            self.current_path = Path("") # this should mean we are at the end of the main file

    def push_frame(self, name: str, pos: tuple[int, int]):
        self.stack.append(StackFrame(name, pos, self.current_path, self.stack[-1].vars, self.stack[-1].funcs))

    def eval_arg(self, tok: str, tok_type: TokenType, pos: tuple[int, int]):
        self.stack[-1].arg(result := eval_token(self, tok, tok_type, pos), pos)
        return result

    def eval_call(self):
        entry = self.stack.pop()
        result = eval_sexp(self, entry)
        if len(self.stack) > 0:
            self.stack[-1].arg(result, entry.pos)
        return result

    def get(self, name: str) -> Any:
        return self.stack[-1].vars[name]

    def set(self, name: str, value: Any):
        for frame in self.stack:
            frame.vars[name] = value

    def call(self, name: str, args: list[Any]) -> Any:
        pos: list[Any] = []
        kw: dict[str, Any] = {}
        next_kw: LispLiteral | None = None
        for arg in args:
            if next_kw is not None:
                kw[str(next_kw)[1:].replace("-", "_")] = arg
                next_kw = None
            elif isinstance(arg, LispLiteral):
                next_kw = arg
            else:
                pos.append(arg)

        return self.stack[-1].funcs[name][0](*pos, **kw)

    def register(self, func: Callable, name: str | None = None, sig: str | None = None, doc: str | None = None):
        info = func_info(func, name, sig, doc)
        for frame in self.stack:
            frame.funcs[info[0]] = info[1:]

    def require(self, filename: str):
        """Require a file to be evaluated.
        Path is relative to the current file."""
        if not filename.endswith(".lisp"):
            filename = filename + ".lisp"
        return parse_file(self.current_path.parent / filename, self)

    def set_lisp(self, sym: LispSymbol, value: Any):
        """Set a variable.
        First argument must be a symbol."""
        if not isinstance(sym, LispSymbol):
            raise ValueError(f"First argument to set must be a symbol! (Did you mean '{sym}?)")
        self.set(sym, value)

    def set_many(self, *args):
        """Set many variables.
        Must have an even number of arguments, with symbol/value pairs."""
        for i in range(0, len(args), 2):
            self.set_lisp(args[i], args[i+1])

def eval_sexp(state: LispState, sexp: StackFrame) -> Any:
    # print(f"call at {sexp.pos} ({sexp.name}{reduce(lambda a, b: a + ' ' + str(b), sexp.args, '')})")
    try:
        result = state.call(sexp.name, sexp.args)
    except Exception as e:
        print(f"{sexp.f.relative_to(state.base_path)}: Error calling function {sexp.name} at line {sexp.pos[0]} column {sexp.pos[1]}:")
        raise e
    return result

def eval_token(state: LispState, tok: str, tok_type: TokenType, pos: tuple[int, int]) -> Any:
    # print(f"eval token {tok} at {pos} with type {tok_type.name}")
    result = None
    try:
        match tok_type:
            case TokenType.NORMAL:
                result = state.get(tok)
            case TokenType.LITERAL:
                result = LispLiteral(tok)
            case TokenType.NUMERIC if '.' in tok:
                result = float(tok)
            case TokenType.NUMERIC:
                result = int(tok)
            case TokenType.STRING:
                result = tok
            case TokenType.SYMBOL:
                result = LispSymbol(tok)
    except Exception as e:
        print(f"Error parsing token {tok} at line {pos[0]} column {pos[1]}:")
        raise e
    return result

def parse_file(fpath, state: LispState | None = None, use_path: bool = True):
    with (open(fpath) as f):
        lines = f.readlines()
    return parse(lines, state, Path(fpath) if use_path else None)

def parse(lines: list[str], state: LispState | None = None, current_file: Path | None = None):
    if state is None:
        assert current_file is not None
        state = LispState(current_file)
    elif current_file is not None:
        state.push_file(current_file)
    # else: use the current file of the state

    parse_state = ParseState.NEXT
    current_tok = ""
    current_pos = (-1, -1)
    current_tok_type = TokenType.NORMAL
    result = None

    def start_tok(row: int, col: int, init = "", tok_type = TokenType.NORMAL):
        nonlocal current_tok, current_pos, current_tok_type
        current_tok = init
        current_pos = (row + 1, col + 1)
        current_tok_type = tok_type

    def eval_arg():
        nonlocal result
        result = state.eval_arg(current_tok, current_tok_type, current_pos)

    for row, line in enumerate(lines):
        if parse_state == ParseState.COMMENT:
            parse_state = ParseState.NEXT
        for col, ch in enumerate(line):
            match parse_state, ch:
                case (s, ';') if s not in (ParseState.STRING_LITERAL, ParseState.STRING_LITERAL_ESCAPE):
                    parse_state = ParseState.COMMENT

                case (ParseState.NEXT, '('): # open new call
                    parse_state = ParseState.CALL
                    start_tok(row, col)
                case (ParseState.CALL, ')'): # no-args call
                    state.push_frame(current_tok, current_pos)
                    result = state.eval_call()
                    parse_state = ParseState.NEXT
                case (ParseState.CALL, c) if c.isspace(): # end of 1+ arg call name
                    state.push_frame(current_tok, current_pos)
                    parse_state = ParseState.NEXT
                case (ParseState.NEXT, ')'): # close call
                    result = state.eval_call()

                case (ParseState.NEXT, "'"):
                    parse_state = ParseState.QUOTE
                case (ParseState.QUOTE, '('): # quoted list
                    state.push_frame("list", (row + 1, col + 1))
                    parse_state = ParseState.NEXT
                case (ParseState.QUOTE, c): # symbol
                    parse_state = ParseState.TOKEN
                    start_tok(row, col, c, TokenType.SYMBOL)

                case (ParseState.NEXT, ':'):
                    parse_state = ParseState.TOKEN
                    start_tok(row, col, "", TokenType.LITERAL)

                case (ParseState.TOKEN, c) if c.isspace(): # end of token
                    eval_arg()
                    parse_state = ParseState.NEXT
                case (ParseState.TOKEN, ')'): # end of token and call
                    eval_arg()
                    result = state.eval_call()
                    parse_state = ParseState.NEXT

                case (ParseState.NEXT, '"'):
                    start_tok(row, col, "", TokenType.STRING)
                    parse_state = ParseState.STRING_LITERAL
                case (ParseState.STRING_LITERAL, '"'):
                    eval_arg()
                    parse_state = ParseState.NEXT
                case (ParseState.STRING_LITERAL, '\\'):
                    parse_state = ParseState.STRING_LITERAL_ESCAPE
                case (ParseState.STRING_LITERAL_ESCAPE, '"'):
                    current_tok += '"'
                    parse_state = ParseState.STRING_LITERAL
                case (ParseState.STRING_LITERAL_ESCAPE, c):
                    current_tok += '\\'
                    current_tok += c
                    parse_state = ParseState.STRING_LITERAL

                case (ParseState.NEXT, c) if c.isdecimal(): # numeric literal
                    start_tok(row, col, c, TokenType.NUMERIC)
                    parse_state = ParseState.TOKEN

                case (ParseState.NEXT, c) if not c.isspace():
                    start_tok(row, col, c)
                    parse_state = ParseState.TOKEN

                case (_, c):
                    current_tok += c

    state.pop_file()
    return result
