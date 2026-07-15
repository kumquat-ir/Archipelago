#!/usr/bin/env python3

import json
import jinja2
from . import interpreter, rule_builder_defs, mod_data_defs, tracker_defs
from pathlib import Path

this_dir = Path(__file__).parent

template_env: jinja2.Environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader([this_dir.parent / "templates", this_dir / "mod" / "templates", this_dir / "tracker" / "templates"])
)

def render(template: str, target: Path, **kwargs) -> None:
    rendered = template_env.get_template(template).render(**kwargs)
    with open(target, "w") as out:
        out.write(rendered)

def render_json(data, target: Path) -> None:
    with open(target, "w") as out:
        json.dump(data, out, indent=4)

rule_builder_defs.use()
(id_mapping, classification_mapping, filler_weights, normal_pool, trimmable, option_pools) = interpreter.parse_file(this_dir / "items.lisp")
render("items.template.py", this_dir.parent / "items.py",
       id_mapping=id_mapping,
       classification_mapping=classification_mapping,
       filler_weights=filler_weights,
       normal_pool=normal_pool,
       trimmable=trimmable,
       option_pools=option_pools)

(region_data,
 (id_mapping, region_mapping, location_rules, events, option_location_regions, option_location_rules),
 goal) = interpreter.parse_file(this_dir / "logic.lisp")
render("regions.template.py", this_dir.parent / "regions.py",
       region_data=region_data)
render("locations.template.py", this_dir.parent / "locations.py",
       id_mapping=id_mapping,
       region_mapping=region_mapping,
       location_rules=location_rules,
       events=events,
       goal=goal,
       option_location_regions=option_location_regions,
       option_location_rules=option_location_rules)

if (this_dir / "mod").exists:
    mod_data_defs.use()
    (decryptor_items, card_items, phase_amounts) = interpreter.parse_file(this_dir / "items.lisp")
    (decryptor_locations, card_locations, ambush_locations, health_locations, phase_locations, orb_locations) = interpreter.parse_file(this_dir / "logic.lisp")
    render("Data.template.cs", this_dir / "mod" / "Data.cs",
           decryptor_items=decryptor_items,
           decryptor_locations=decryptor_locations,
           phase_amounts=phase_amounts,
           card_items=card_items,
           card_locations=card_locations,
           ambush_locations=ambush_locations,
           health_locations=health_locations,
           phase_locations=phase_locations,
           orb_locations=orb_locations)
else:
    print("Not rendering mod files, logic/mod not found")

if (this_dir / "tracker").exists:
    tracker_defs.use()
    (item_mapping, item_data) = interpreter.parse_file(this_dir / "items.lisp")
    render("item_mapping.template.lua", this_dir / "tracker" / "scripts" / "autotracking" / "item_mapping.lua",
           item_mapping=item_mapping)
    render_json(item_data, this_dir / "tracker" / "items" / "items.json")

    (location_mapping, location_data) = interpreter.parse_file(this_dir / "logic.lisp")
    render("location_mapping.template.lua", this_dir / "tracker" / "scripts" / "autotracking" / "location_mapping.lua",
           location_mapping=location_mapping)
    render_json(location_data, this_dir / "tracker" / "locations" / "locations.json")
else:
    print("Not rendering tracker files, logic/tracker not found")
