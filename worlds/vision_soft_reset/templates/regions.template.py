# This file is generated, do not edit!
# Instead see templates/regions.template.py and logic/regions.lisp

from worlds.AutoWorld import World
from BaseClasses import Region
from rule_builder.rules import Rule, Has, HasAll, HasAny, OptionFilter, True_, CanReachRegion, CanReachEntrance
from .options import HardLogic, RequireBossCards

REGION_DATA: dict[str, dict[str, Rule | None] | None] = {
    {%- for name, connections in region_data.items() %}
    "{{ name }}":
    {%- if connections|length > 0 %} {
    {%- for region, rule in connections.items() %}
        "{{ region }}": {{ rule }},
    {%- endfor %}
    },
    {%- else %} None,
    {%- endif %}
    {%- endfor %}
}

def create_regions(world: World) -> None:
    regions: list[Region] = []

    for name in REGION_DATA.keys():
        regions.append(Region(name, world.player, world.multiworld))

    world.multiworld.regions += regions

def connect_regions(world: World) -> None:
    for name, connections in REGION_DATA.items():
        if connections is None:
            continue
        region = world.get_region(name)
        for dest_name, rule in connections.items():
            region.connect(world.get_region(dest_name), rule=rule)
