# This file is generated, do not edit!
# Instead see templates/locations.template.py and logic/locations.lisp

from .items import VSRItem
from .options import HardLogic, RequireBossCards
from worlds.AutoWorld import World
from BaseClasses import Location
from rule_builder.rules import Rule, Has, HasAll, HasAny, OptionFilter, True_, CanReachRegion, CanReachEntrance

LOCATION_ID_MAP: dict[str, int] = {
{%- for location, id in id_mapping.items() %}
    "{{ location }}": {{ id }},
{%- endfor %}
}

LOCATION_REGION_MAP: dict[str, dict[str, int]] = {
{%- for region, locations in region_mapping.items() %}
    "{{ region }}": {
    {%- for location, id in locations.items() %}
        "{{ location }}": {{ id }},
    {%- endfor %}
    },
{%- endfor %}
}

LOCATION_RULES: dict[str, Rule] = {
{%- for location, rule in location_rules.items() %}
    "{{ location }}": {{ rule }},
{%- endfor %}
}

EVENTS: dict[str, dict[str, str]] = {
{%- for region, event in events.items() %}
    "{{ region }}": {
    {%- for location_name, event_name in event.items() %}
        "{{ location_name }}": "{{ event_name }}",
    {%- endfor %}
    },
{%- endfor %}
}

OPTION_LOCATION_REGION_MAP: dict[str, dict[str, dict[str, int]]] = {
{%- for option, mapping in option_location_regions.items() %}
    "{{ option }}": {
    {%- for region, locations in mapping.items() %}
        "{{ region }}": {
        {%- for location, id in locations.items() %}
            "{{ location }}": {{ id }},
        {%- endfor %}
        },
    {%- endfor %}
    },
{%- endfor %}
}

OPTION_LOCATION_RULES: dict[str, dict[str, Rule]] = {
{%- for option, rules in option_location_rules.items() %}
    "{{ option }}": {
    {%- for location, rule in rules.items() %}
        "{{ location }}": {{ rule }},
    {%- endfor %}
    },
{%- endfor %}
}

GOAL: Rule = {{ goal }}

class VSRLocation(Location):
    game = "Vision Soft Reset"

def create_locations(world: World) -> None:
    for region_name, locations in LOCATION_REGION_MAP.items():
        world.get_region(region_name).add_locations(locations, VSRLocation)

    for option, region_mapping in OPTION_LOCATION_REGION_MAP.items():
        if not getattr(world.options, option).value:
            continue
        for region_name, locations in region_mapping.items():
            world.get_region(region_name).add_locations(locations, VSRLocation)

    for region_name, events in EVENTS.items():
        region = world.get_region(region_name)
        for event_location, event_item in events.items():
            region.add_event(event_location, event_item, location_type=VSRLocation, item_type=VSRItem)

def set_rules(world: World) -> None:
    for location, rule in LOCATION_RULES.items():
        world.set_rule(world.get_location(location), rule)

    for option, rules in OPTION_LOCATION_RULES.items():
        if not getattr(world.options, option).value:
            continue
        for location, rule in rules.items():
            world.set_rule(world.get_location(location), rule)

    world.set_completion_rule(GOAL)
