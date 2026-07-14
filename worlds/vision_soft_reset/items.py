# This file is generated, do not edit!
# Instead see templates/items.template.py and logic/items.lisp

from Options import Option
from worlds.AutoWorld import World
from typing import TYPE_CHECKING, Callable
from BaseClasses import ItemClassification, Item

ITEM_ID_MAP: dict[str, int] = {
    "Phase Refill (25%)": 1,
    "Phase Refill (50%)": 2,
    "Phase Refill (75%)": 3,
    "Phase Refill (100%)": 4,
    "Charge Shot": 100,
    "Charge Magnet": 101,
    "Altered Shot": 102,
    "Charge Grip": 103,
    "Wall Run": 104,
    "Spin Dodge": 105,
    "Heat Resist": 106,
    "Mental Recovery": 107,
    "Energy Claw": 108,
    "Strip Suit": 109,
    "Shell Escape": 110,
    "Speed Boost": 111,
    "Vile Claw": 112,
    "Piercing Speed": 113,
    "Golden View": 114,
    "d#Z 5~qn. P": 115,
    "Virus Wipe": 116,
    "Double Shot": 117,
    "Spin Double": 118,
    "Twister Jump": 119,
    "Chamber Focus": 120,
    "Engine Tune": 121,
    "Card: Magoom": 201,
    "Card: Ciurivy": 202,
    "Card: Smosey": 203,
    "Card: Wavemoth": 204,
    "Card: Midow": 205,
    "Card: Prittle": 206,
    "Card: Sealime": 207,
    "Card: Toucade": 208,
    "Card: Shaifi": 209,
    "Card: Pengrunt": 210,
    "Card: Cottospark": 211,
    "Card: Cottocache": 212,
    "Card: Drilbas": 213,
    "Card: Jinvell": 214,
    "Card: Royalrose": 215,
    "Card: Rupo": 216,
    "Card: Froesburn": 217,
    "Card: Ghostily": 218,
    "Card: Sherivice": 219,
    "Card: Griger": 220,
    "Card: Solatia": 221,
    "Card: Salesman": 222,
    "Card: Oracle": 223,
    "Card: Oracle-L": 224,
}

ITEM_CLASSIFICATIONS: dict[str, ItemClassification | Callable[[World], ItemClassification]] = {
    "Phase Refill (25%)": ItemClassification.filler,
    "Phase Refill (50%)": ItemClassification.filler,
    "Phase Refill (75%)": ItemClassification.filler,
    "Phase Refill (100%)": ItemClassification.filler,
    "Charge Shot": ItemClassification.progression,
    "Charge Magnet": ItemClassification.useful,
    "Altered Shot": ItemClassification.useful,
    "Charge Grip": ItemClassification.useful,
    "Wall Run": ItemClassification.progression,
    "Spin Dodge": ItemClassification.progression,
    "Heat Resist": ItemClassification.progression,
    "Mental Recovery": ItemClassification.useful,
    "Energy Claw": ItemClassification.progression,
    "Strip Suit": ItemClassification.progression,
    "Shell Escape": ItemClassification.useful,
    "Speed Boost": ItemClassification.progression,
    "Vile Claw": ItemClassification.progression,
    "Piercing Speed": ItemClassification.progression,
    "Golden View": ItemClassification.filler,
    "d#Z 5~qn. P": ItemClassification.progression,
    "Virus Wipe": ItemClassification.filler,
    "Double Shot": ItemClassification.useful,
    "Spin Double": ItemClassification.progression,
    "Twister Jump": ItemClassification.progression,
    "Chamber Focus": ItemClassification.useful,
    "Engine Tune": ItemClassification.progression,
    "Card: Magoom": ItemClassification.useful,
    "Card: Ciurivy": ItemClassification.useful,
    "Card: Smosey": ItemClassification.useful,
    "Card: Wavemoth": ItemClassification.useful,
    "Card: Midow": ItemClassification.useful,
    "Card: Prittle": ItemClassification.useful,
    "Card: Sealime": ItemClassification.useful,
    "Card: Toucade": ItemClassification.useful,
    "Card: Shaifi": ItemClassification.filler,
    "Card: Pengrunt": ItemClassification.useful,
    "Card: Cottospark": ItemClassification.useful,
    "Card: Cottocache": ItemClassification.useful,
    "Card: Drilbas": ItemClassification.filler,
    "Card: Jinvell": ItemClassification.useful,
    "Card: Royalrose": ItemClassification.useful,
    "Card: Rupo": ItemClassification.useful,
    "Card: Froesburn": ItemClassification.useful,
    "Card: Ghostily": ItemClassification.filler,
    "Card: Sherivice": ItemClassification.filler,
    "Card: Griger": lambda world: ItemClassification.progression if getattr(world.options, "require_boss_cards").value else ItemClassification.useful,
    "Card: Solatia": lambda world: ItemClassification.progression if getattr(world.options, "require_boss_cards").value else ItemClassification.useful,
    "Card: Salesman": lambda world: ItemClassification.progression if getattr(world.options, "require_boss_cards").value else ItemClassification.useful,
    "Card: Oracle": ItemClassification.filler,
    "Card: Oracle-L": ItemClassification.filler,
}

FILLER_WEIGHTS: dict[str, int] = {
    "Phase Refill (25%)": 50,
    "Phase Refill (50%)": 25,
    "Phase Refill (75%)": 15,
    "Phase Refill (100%)": 10,
}

NORMAL_POOL: list[str] = [
    "Charge Shot",
    "Charge Magnet",
    "Altered Shot",
    "Charge Grip",
    "Wall Run",
    "Spin Dodge",
    "Heat Resist",
    "Mental Recovery",
    "Energy Claw",
    "Strip Suit",
    "Shell Escape",
    "Speed Boost",
    "Vile Claw",
    "Piercing Speed",
    "Golden View",
    "d#Z 5~qn. P",
    "Virus Wipe",
    "Double Shot",
    "Card: Magoom",
    "Card: Ciurivy",
    "Card: Smosey",
    "Card: Wavemoth",
    "Card: Midow",
    "Card: Prittle",
    "Card: Sealime",
    "Card: Toucade",
    "Card: Shaifi",
    "Card: Pengrunt",
    "Card: Cottospark",
    "Card: Cottocache",
    "Card: Drilbas",
    "Card: Jinvell",
    "Card: Royalrose",
    "Card: Rupo",
    "Card: Froesburn",
    "Card: Ghostily",
    "Card: Sherivice",
    "Card: Griger",
    "Card: Solatia",
    "Card: Salesman",
    "Card: Oracle",
    "Card: Oracle-L",
]

TRIMMABLE: list[str] = [
    "Card: Shaifi",
    "Card: Drilbas",
    "Card: Oracle",
    "Card: Oracle-L",
]

OPTION_POOLS: dict[str, list[str]] = {
    "extra_decryptors": [
        "Spin Double",
        "Twister Jump",
        "Chamber Focus",
        "Engine Tune",
    ],
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