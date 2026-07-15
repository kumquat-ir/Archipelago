from typing import Any
import dataclasses
import itertools
from .interpreter import LispState, LispSymbol

# classes for DNF reduction

class CondTrue:
    pass

@dataclasses.dataclass
class And:
    clauses: list[str]

    @staticmethod
    def of(*clauses_in):
        clauses = []
        ors = []

        for clause in clauses_in:
            if clause is None or isinstance(clause, CondTrue):
                continue
            elif isinstance(clause, And):
                clauses.extend(clause.clauses)
            elif isinstance(clause, Or):
                ors.append(clause)
            else:
                clauses.append(clause)

        if len(ors) == 0:
            return And(clauses)

        resolved = []
        for combo in itertools.product(*[o.clauses for o in ors]):
            resolved.append(And.of(*(clauses + list(combo))))
        return Or.of(*resolved)

@dataclasses.dataclass
class Or:
    clauses: list[And]

    @staticmethod
    def of(*clauses_in):
        clauses = []

        for clause in clauses_in:
            if isinstance(clause, Or):
                clauses.extend(clause.clauses)
            else:
                clauses.append(And.of(clause))

        return Or(clauses)

@dataclasses.dataclass
class ItemInfo:
    name: str
    id: int
    code: str
    is_progression: bool
    kind: str

@dataclasses.dataclass
class LocationInfo:
    name: str
    id: int
    region: str
    group: str | None
    coords: tuple[float, float] | None
    condition: And | Or | None
    visibility: And | Or | None

@dataclasses.dataclass
class RegionInfo:
    name: str
    connections: dict[str, And | Or | None]
    reverse_connections: list[And | Or | None]

def resolve_condition(cond: And | Or | None) -> list[str] | None:
    if isinstance(cond, And):
        cond = Or.of(cond)
    if isinstance(cond, Or):
        seen: list[list[str]] = []
        for clause in cond.clauses:
            deduped = list(dict.fromkeys(clause.clauses).keys())
            to_del = []
            for prev in seen:
                if all([(c in deduped) for c in prev]):
                    # deduped is a superset of a condition we've already seen: we can discard it
                    break
                elif all([(c in prev) for c in deduped]):
                    # deduped is a subset of a condition we've already seen: discard that one
                    to_del.append(prev)
            else:
                for it in to_del:
                    seen.remove(it)
                seen.append(deduped)

        return [
            ",".join(conditions)
            for conditions in seen
        ]
    return None

def item_code(item_name: str) -> str:
    return item_name.lower().replace(' ', '').replace(':', '-')

def items(*names: str) -> And:
    return And.of(*[item_code(name) for name in names])

def any_item(*names: str) -> Or:
    return Or.of(*[item_code(name) for name in names])

def _or(*args) -> Or:
    return Or.of(*args)

def _and(*args) -> And | Or:
    return And.of(*args)

def _true() -> CondTrue:
    return CondTrue()

def region_access(region: str) -> And:
    return And.of(at_location(region))

entrances_to_generate: list[tuple[str, str]] = []
def entrance_access(from_region: str, to_region: str):
    entrances_to_generate.append((from_region, to_region))
    return And.of(at_location(from_region) + " -> " + to_region)

def option(option: str | LispSymbol, value: bool):
    return And.of(f"$option|{item_code(option)}|{item_code(str(value))}")

def includes_progression(*args) -> str:
    if "progression" in args:
        return "progression"
    return "filler"

def item(name: str, id: int, classifications: LispSymbol | list[LispSymbol] | str, **kwargs) -> ItemInfo | None:
    if isinstance(classifications, list):
        classifications = includes_progression(*classifications)

    kind = "other"
    if "decryptor_id" in kwargs:
        kind = "decryptor"
    elif "card_id" in kwargs:
        kind = "card"

    return ItemInfo(name, id, item_code(name), classifications == "progression", kind)

def item_list(*items: ItemInfo | None) -> tuple[dict[int, str], list]:
    item_mapping = {item.id: item.code for item in items if item is not None and item.is_progression}
    item_data = [
        {
            "name": item.name,
            "type": "toggle",
            "img": f"images/{item.kind}.png",
            "codes": item.code
        }
        for item in items
        if item is not None and item.is_progression
    ]

    return (item_mapping, item_data)

def location(name: str, id: int, *,
             region: str,
             tracker_group: str | None = None,
             coords: list[float] | None = None,
             ambush_coords: list[int] | None = None,
             condition: And | Or | None = None,
             include_option: str | None = None,
             **_kwargs) -> LocationInfo:
    real_coords = coords or ambush_coords
    if real_coords is not None:
        real_coords = tuple(real_coords)
        assert len(real_coords) == 2
    return LocationInfo(name, id, region, tracker_group, real_coords, condition, option(include_option, True) if include_option is not None else None)

def event(location_name: str, item_name: str, region: str, *, coords, condition, include_option = None, **_kwargs) -> LocationInfo:
    return LocationInfo(item_name, 0, region, location_name, tuple(coords), condition, option(include_option, True) if include_option is not None else None)

def map_location(coords: tuple[float, float]) -> dict:
    return {
        "map": "map",
        "x": int(4 * (coords[0] * 9 - 4.5)),
        "y": int(4 * (216 - (coords[1] * 6 - 3)))
    }

def at_location(region: str, group: str | None = None, name: str | None = None) -> str:
    return f"@{region}{'/' + group if group is not None else ''}{'/' + name if name is not None else ''}{'/' if group is None and name is not None else ''}"

def location_list(*locations: LocationInfo | None) -> tuple[dict[int, str], dict[str, list[Any]], dict[str, int]]:
    location_mapping = {loc.id: at_location(loc.region, loc.group, loc.name) for loc in locations if loc is not None and loc.id != 0}
    ut_mapping = {loc.name + '/': loc.id for loc in locations if loc is not None and loc.group is None}

    location_data: dict[str, list[Any]] = {}
    groups: dict[str, Any] = {}
    for location in locations:
        if location is None:
            continue

        if location.region not in location_data:
            location_data[location.region] = []

        if location.group is not None:
            if location.group not in groups:
                groups[location.group] = {
                    "name": location.group,
                    "access_rules": None,
                    "sections": []
                }
                location_data[location.region].append(groups[location.group])
            if location.coords is not None:
                groups[location.group]["map_locations"] = [map_location(location.coords)]
            groups[location.group]["sections"].append({
                "name": location.name,
                "access_rules": resolve_condition(location.condition),
                "visibility_rules": resolve_condition(location.visibility),
                "item_count": 1
            })

        else:
            assert location.coords is not None
            location_data[location.region].append({
                "name": location.name,
                "access_rules": resolve_condition(location.condition),
                "map_locations": [map_location(location.coords)],
                "visibility_rules": resolve_condition(location.visibility),
                "sections": [{
                    "name": "",
                    "item_count": 1
                }]
            })

    return (location_mapping, location_data, ut_mapping)

def connection(to: str, condition: str | None = None) -> tuple[str, str | None]:
    return (to, condition)

def region(name: str, *connections) -> RegionInfo:
    return RegionInfo(name, dict(connections), [])

def region_list(*regions: RegionInfo) -> dict[str, dict]:
    reverse_connections: dict[str, dict[str, And | Or | None]] = {}
    entrances: list[RegionInfo] = []
    for region in regions:
        for connection in region.connections:
            if connection not in reverse_connections:
                reverse_connections[connection] = {}
            reverse_connections[connection][region.name] = region.connections[connection]

            if (region.name, connection) in entrances_to_generate:
                entrances.append(RegionInfo(f"{region.name} -> {connection}", {}, [And.of(region_access(region.name), region.connections[connection])]))

    for region in regions:
        connections = reverse_connections[region.name] if region.name in reverse_connections else {}
        region.reverse_connections = [
            And.of(at_location(connection), rule)
            for (connection, rule) in connections.items()
        ]


    return {
        region.name: {
            "name": region.name,
            "access_rules": resolve_condition(Or.of(*region.reverse_connections)),
            "children": []
        }
        for region in (list(regions) + entrances)
    }

def logic_data(regions: dict[str, dict], locations: tuple[dict, dict, dict], **_kwargs) -> tuple[dict, list, dict]:
    for location in locations[1]:
        regions[location]["children"].extend(locations[1][location])
    return (locations[0], list(regions.values()), locations[2])

def use() -> None:
    global entrances_to_generate
    entrances_to_generate = []
    LispState.reset()
    LispState.register_global(includes_progression, "if-option")
    LispState.register_global(item)
    LispState.register_global(item_list, "item-list")
    LispState.register_global(items)
    LispState.register_global(any_item, "any-item")
    LispState.register_global(region_access, "region?")
    LispState.register_global(entrance_access, "entrance?")
    LispState.register_global(_and, "and")
    LispState.register_global(_or, "or")
    LispState.register_global(_true, "true")
    LispState.register_global(option)
    LispState.register_global(location)
    LispState.register_global(event)
    LispState.register_global(location_list, "location-list")
    LispState.register_global(connection, "->")
    LispState.register_global(region)
    LispState.register_global(region_list, "region-list")
    LispState.register_global(logic_data, "logic-data")
