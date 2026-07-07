#!/usr/bin/env python3

import jinja2
from . import interpreter, rule_builder_defs, mod_data_defs
from pathlib import Path

this_dir = Path(__file__).parent

template_env: jinja2.Environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader([this_dir.parent / "templates", this_dir / "mod" / "templates"])
)

def render(template: str, target: Path, **kwargs) -> None:
    rendered = template_env.get_template(template).render(**kwargs)
    with open(target, "w") as out:
        out.write(rendered)

rule_builder_defs.use()
(id_mapping, classification_mapping, filler_weights, normal_pool, trimmable, option_pools) = interpreter.parse_file(this_dir / "items.lisp")
render("items.template.py", this_dir.parent / "items.py",
       id_mapping=id_mapping,
       classification_mapping=classification_mapping,
       filler_weights=filler_weights,
       normal_pool=normal_pool,
       trimmable=trimmable,
       option_pools=option_pools)

(region_data, (id_mapping, region_mapping, rules, events), goal) = interpreter.parse_file(this_dir / "logic.lisp")
render("regions.template.py", this_dir.parent / "regions.py",
       region_data=region_data)
render("locations.template.py", this_dir.parent / "locations.py",
       id_mapping=id_mapping,
       region_mapping=region_mapping,
       rules=rules,
       events=events,
       goal=goal)

mod_data_defs.use()
(decryptor_items, card_items) = interpreter.parse_file(this_dir / "items.lisp")
(decryptor_locations, card_locations) = interpreter.parse_file(this_dir / "logic.lisp")
render("Data.template.cs", this_dir / "mod" / "Data.cs",
       decryptor_items=decryptor_items,
       decryptor_locations=decryptor_locations,
       card_items=card_items,
       card_locations=card_locations)
