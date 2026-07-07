# This file is generated, do not edit!
# Instead see templates/items.template.py and logic/items.lisp

from Options import Option
from worlds.AutoWorld import World
from typing import TYPE_CHECKING, Callable
from BaseClasses import ItemClassification, Item

ITEM_ID_MAP: dict[str, int] = {
{%- for item, id in id_mapping.items() %}
    "{{ item }}": {{ id }},
{%- endfor %}
}

ITEM_CLASSIFICATIONS: dict[str, ItemClassification | Callable[[World], ItemClassification]] = {
{%- for item, classification in classification_mapping.items() %}
    "{{ item }}": {{ classification }},
{%- endfor %}
}

FILLER_WEIGHTS: dict[str, int] = {
{%- for item, weight in filler_weights.items() %}
    "{{ item }}": {{ weight }},
{%- endfor %}
}

NORMAL_POOL: list[str] = [
{%- for item in normal_pool %}
    "{{ item }}",
{%- endfor %}
]

TRIMMABLE: list[str] = [
{%- for item in trimmable %}
    "{{ item }}",
{%- endfor %}
]

OPTION_POOLS: dict[str, list[str]] = {
{%- for option, pool in option_pools.items() %}
    "{{ option }}": [
    {%- for item in pool %}
        "{{ item }}",
    {%- endfor %}
    ],
{%- endfor %}
}

class VSRItem(Item):
    game = "Vision Soft Reset"

def random_filler_item_name(world: World) -> str:
    return world.random.choices(list(FILLER_WEIGHTS.keys()), list(FILLER_WEIGHTS.values()))[0]

def create_item(world: World, name: str) -> VSRItem:
    classification = ITEM_CLASSIFICATIONS.get(name, ItemClassification.filler)
    if not isinstance(classification, ItemClassification):
        classification = classification(world)
    return VSRItem(name, classification, ITEM_ID_MAP[name], world.player)

def fill_item_pool(world: World) -> None:
    pool: list[Item] = []
    staged_pool: list[str] = []

    staged_pool += NORMAL_POOL

    for option, option_pool in OPTION_POOLS.items():
        if getattr(world.options, option).value:
            staged_pool += option_pool

    needed_trims = len(staged_pool) - len(world.multiworld.get_unfilled_locations(world.player))
    if needed_trims > 0:
        # more items than locations! thankfully, we have a list of items that are safe to remove, so do that first
        to_trim = TRIMMABLE[:]
        for _ in range(max(len(TRIMMABLE) - needed_trims, 0)):
            to_trim.pop(world.random.randint(0, 1-len(to_trim)))
        for trim in to_trim:
            staged_pool.remove(trim)

    pool += [world.create_item(item) for item in staged_pool]
    needed_filler = len(world.multiworld.get_unfilled_locations(world.player)) - len(pool)
    pool += [world.create_filler() for _ in range(needed_filler)]

    world.multiworld.itempool += pool
