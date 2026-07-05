#!/usr/bin/env python3

import jinja2
from . import interpreter, item_defs, rule_builder_defs
from pathlib import Path

this_dir = Path(__file__).parent

template_env: jinja2.Environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(this_dir.parent / "templates")
)

def render(template: str, target: Path, **kwargs) -> None:
    rendered = template_env.get_template(template).render(**kwargs)
    with open(target, "w") as out:
        out.write(rendered)

item_defs.use()
(id_mapping, classification_mapping, filler_weights, normal_pool, trimmable, option_pools) = interpreter.parse_file(this_dir / "items.lisp")
render("items.template.py", this_dir.parent / "items.py",
       id_mapping=id_mapping,
       classification_mapping=classification_mapping,
       filler_weights=filler_weights,
       normal_pool=normal_pool,
       trimmable=trimmable,
       option_pools=option_pools)

rule_builder_defs.use()
(region_data, (id_mapping, region_mapping, rules, events), goal) = interpreter.parse_file(this_dir / "logic.lisp")
render("regions.template.py", this_dir.parent / "regions.py",
       region_data=region_data)
render("locations.template.py", this_dir.parent / "locations.py",
       id_mapping=id_mapping,
       region_mapping=region_mapping,
       rules=rules,
       events=events,
       goal=goal)
