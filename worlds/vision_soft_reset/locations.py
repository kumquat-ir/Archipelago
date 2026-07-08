# This file is generated, do not edit!
# Instead see templates/locations.template.py and logic/locations.lisp

from .items import VSRItem
from .options import HardLogic, RequireBossCards
from worlds.AutoWorld import World
from BaseClasses import Location
from rule_builder.rules import Rule, Has, HasAll, HasAny, OptionFilter, True_, CanReachRegion, CanReachEntrance

LOCATION_ID_MAP: dict[str, int] = {
    "Decryptor: Charge Shot": 100,
    "Decryptor: Charge Magnet": 101,
    "Decryptor: Altered Shot": 102,
    "Decryptor: Charge Grip": 103,
    "Decryptor: Wall Run": 104,
    "Decryptor: Spin Dodge": 105,
    "Decryptor: Heat Resist": 106,
    "Decryptor: Mental Recovery": 107,
    "Decryptor: Energy Claw": 108,
    "Decryptor: Strip Suit": 109,
    "Decryptor: Shell Escape": 110,
    "Decryptor: Speed Boost": 111,
    "Decryptor: Vile Claw": 112,
    "Decryptor: Piercing Speed": 113,
    "Decryptor: Golden View": 114,
    "Decryptor: d#Z 5~qn. P": 115,
    "Decryptor: Virus Wipe": 116,
    "Decryptor: Double Shot": 117,
    "Card 01: Magoom": 201,
    "Card 02: Ciurivy": 202,
    "Card 03: Smosey": 203,
    "Card 04: Wavemoth": 204,
    "Card 05: Midow": 205,
    "Card 06: Prittle": 206,
    "Card 07: Sealime": 207,
    "Card 08: Toucade": 208,
    "Card 09: Shaifi": 209,
    "Card 10: Pengrunt": 210,
    "Card 11: Cottospark": 211,
    "Card 12: Cottocache": 212,
    "Card 13: Drilbas": 213,
    "Card 14: Jinvell": 214,
    "Card 15: Royalrose": 215,
    "Card 16: Rupo": 216,
    "Card 17: Froesburn": 217,
    "Card 18: Ghostily": 218,
    "Card 19: Sherivice": 219,
    "Card 20: Griger": 220,
    "Card 21: Solatia": 221,
    "Card 22: Salesman": 222,
    "Card 23: Oracle": 223,
    "Card 24: Oracle-L": 224,
    "First Ambush": 300,
    "Ambush Before Charge Shot": 301,
    "Power Area Lower Ambush": 302,
    "Power Area Upper Ambush": 303,
    "Pre-Spin Dodge Ambush": 304,
    "Cottospark Ambush": 305,
    "Block Puzzle Ambush": 306,
    "Underwater Ambush": 307,
    "Claw Bounce Ambush": 308,
    "Floatlands Ambush": 309,
    "First Health Upgrade": 400,
    "Pre-Spin Dodge Health Upgrade": 401,
    "Floatlands Health Upgrade": 402,
    "Warehouse Entry Health Upgrade": 403,
    "Phase Upgrade Left of Ship": 404,
    "Phase Upgrade Outside Griger's Base": 405,
    "Lower Mountain Phase Upgrade": 406,
    "Upper Mountain Phase Upgrade": 407,
    "Orb A": 408,
    "Orb B": 409,
    "Orb C": 410,
    "Orb D": 411,
}

LOCATION_REGION_MAP: dict[str, dict[str, int]] = {
    "Ship": {
        "Decryptor: Charge Shot": 100,
        "Decryptor: Charge Magnet": 101,
        "Card 02: Ciurivy": 202,
        "Card 07: Sealime": 207,
        "Card 24: Oracle-L": 224,
    },
    "Above First Puzzle": {
        "Decryptor: Altered Shot": 102,
    },
    "Power Area": {
        "Decryptor: Charge Grip": 103,
        "Decryptor: Golden View": 114,
        "Card 01: Magoom": 201,
    },
    "Wall Run Area": {
        "Decryptor: Wall Run": 104,
    },
    "Spin Dodge Area": {
        "Decryptor: Spin Dodge": 105,
    },
    "Mountain Chamber": {
        "Decryptor: Heat Resist": 106,
    },
    "Lower Floatlands": {
        "Decryptor: Mental Recovery": 107,
    },
    "Griger": {
        "Decryptor: Energy Claw": 108,
        "Card 20: Griger": 220,
    },
    "Warehouse": {
        "Decryptor: Strip Suit": 109,
        "Decryptor: Virus Wipe": 116,
    },
    "Underwater": {
        "Decryptor: Shell Escape": 110,
        "Card 18: Ghostily": 218,
    },
    "Solatia Run": {
        "Decryptor: Speed Boost": 111,
    },
    "Hot Water Area": {
        "Decryptor: Vile Claw": 112,
    },
    "Upper Mountain": {
        "Decryptor: Piercing Speed": 113,
        "Card 22: Salesman": 222,
    },
    "Orb C": {
        "Decryptor: d#Z 5~qn. P": 115,
    },
    "Mountain Water Run": {
        "Decryptor: Double Shot": 117,
    },
    "Past First Puzzle": {
        "Card 03: Smosey": 203,
        "Card 05: Midow": 205,
        "Card 08: Toucade": 208,
    },
    "Griger's Base (Right)": {
        "Card 04: Wavemoth": 204,
    },
    "First Puzzle Solution": {
        "Card 06: Prittle": 206,
    },
    "Beach": {
        "Card 09: Shaifi": 209,
        "Card 14: Jinvell": 214,
    },
    "Griger's Base (Powerless Room)": {
        "Card 10: Pengrunt": 210,
    },
    "Above Orb A": {
        "Card 11: Cottospark": 211,
        "Card 12: Cottocache": 212,
    },
    "Left of Ship": {
        "Card 13: Drilbas": 213,
    },
    "Upper Floatlands": {
        "Card 15: Royalrose": 215,
    },
    "Orb B": {
        "Card 16: Rupo": 216,
    },
    "Mountain Fall": {
        "Card 17: Froesburn": 217,
    },
    "Right Floatlands": {
        "Card 19: Sherivice": 219,
    },
    "Solatia": {
        "Card 21: Solatia": 221,
    },
    "Orb D": {
        "Card 23: Oracle": 223,
    },
}

LOCATION_RULES: dict[str, Rule] = {
    "Decryptor: Charge Magnet": (Has("Charge Shot") | HasAll("Energy Claw", "Vile Claw")),
    "Decryptor: Heat Resist": (HasAny("Wall Run", "Spin Dodge") & (Has("Charge Shot") | HasAll("Energy Claw", "Vile Claw")) & (CanReachEntrance("Above First Puzzle -> Mountain Chamber") | (CanReachEntrance("Ship -> Mountain Water Run") & CanReachEntrance("Mountain Water Run -> Mountain Chamber")))),
    "Decryptor: Energy Claw": (HasAny("Wall Run", "Spin Dodge") & (OptionFilter(RequireBossCards, False) | Has("Card: Griger"))),
    "Decryptor: Strip Suit": (HasAll("Wall Run", "Spin Dodge") & Has("d#Z 5~qn. P")),
    "Decryptor: Shell Escape": Has("Strip Suit"),
    "Decryptor: Vile Claw": Has("Energy Claw"),
    "Decryptor: Piercing Speed": (HasAll("Wall Run", "Spin Dodge") & (Has("Speed Boost") | HasAll("Spin Double", "Twister Jump"))),
    "Decryptor: Golden View": CanReachRegion("Power Area"),
    "Decryptor: Virus Wipe": (HasAll("Wall Run", "Spin Dodge") & Has("d#Z 5~qn. P")),
    "Decryptor: Double Shot": Has("Speed Boost"),
    "Card 01: Magoom": CanReachRegion("Power Area"),
    "Card 03: Smosey": (HasAll("Wall Run", "Spin Dodge") & (OptionFilter(HardLogic, True) | Has("Charge Shot"))),
    "Card 04: Wavemoth": HasAny("Wall Run", "Spin Dodge"),
    "Card 07: Sealime": (HasAll("Speed Boost", "Wall Run") | (HasAll("Spin Dodge", "Spin Double") & Has("Wall Run"))),
    "Card 08: Toucade": Has("Spin Dodge"),
    "Card 11: Cottospark": (Has("Speed Boost") & HasAny("Wall Run", "Spin Dodge")),
    "Card 12: Cottocache": (Has("Speed Boost") & HasAny("Wall Run", "Spin Dodge")),
    "Card 13: Drilbas": HasAll("Wall Run", "Spin Dodge"),
    "Card 14: Jinvell": HasAll("Speed Boost", "Wall Run", "Spin Dodge"),
    "Card 16: Rupo": HasAll("Speed Boost", "Wall Run"),
    "Card 17: Froesburn": Has("Strip Suit"),
    "Card 18: Ghostily": Has("Strip Suit"),
    "Card 20: Griger": (HasAny("Wall Run", "Spin Dodge") & Has("Energy Claw") & (OptionFilter(RequireBossCards, False) | Has("Card: Griger"))),
    "Card 22: Salesman": (CanReachRegion("Ship") & CanReachRegion("First Puzzle Solution") & CanReachRegion("Past First Puzzle") & CanReachRegion("Endoplanetary Shield") & CanReachRegion("Power Area") & CanReachRegion("Griger's Base (Top)") & CanReachRegion("Underwater") & CanReachRegion("Orb A") & CanReachRegion("Claw Bounce Area") & CanReachRegion("Floatlands Entry") & CanReachRegion("Solatia Run") & CanReachRegion("Mountain Chamber") & CanReachRegion("Mountain Fall") & CanReachRegion("Warehouse") & (CanReachEntrance("Warehouse -> Hot Water Area") & CanReachEntrance("Hot Water Area -> Endoplanetary Shield") & CanReachEntrance("Endoplanetary Shield -> Past First Puzzle")) & CanReachRegion("Mountaintop")),
    "Card 24: Oracle-L": Has("Strip Suit"),
    "Defeat Salesman": (OptionFilter(RequireBossCards, False) | Has("Card: Salesman")),
}

EVENTS: dict[str, dict[str, str]] = {
    "Mountaintop": {
        "Defeat Salesman": "Victory",
    },
}

OPTION_LOCATION_REGION_MAP: dict[str, dict[str, dict[str, int]]] = {
    "add_ambushes": {
        "Ship": {
            "First Ambush": 300,
            "Ambush Before Charge Shot": 301,
        },
        "Power Area": {
            "Power Area Lower Ambush": 302,
        },
        "Under Beach": {
            "Power Area Upper Ambush": 303,
        },
        "Pre-Spin Dodge": {
            "Pre-Spin Dodge Ambush": 304,
        },
        "Griger's Base (Right)": {
            "Cottospark Ambush": 305,
        },
        "Griger's Base (Bottom Left)": {
            "Block Puzzle Ambush": 306,
        },
        "Underwater": {
            "Underwater Ambush": 307,
        },
        "Claw Bounce Area": {
            "Claw Bounce Ambush": 308,
        },
        "Floatlands Ambush": {
            "Floatlands Ambush": 309,
        },
    },
    "add_physical": {
        "Ship": {
            "First Health Upgrade": 400,
        },
        "Pre-Spin Dodge": {
            "Pre-Spin Dodge Health Upgrade": 401,
        },
        "Upper Floatlands": {
            "Floatlands Health Upgrade": 402,
        },
        "Warehouse": {
            "Warehouse Entry Health Upgrade": 403,
        },
        "Left of Ship": {
            "Phase Upgrade Left of Ship": 404,
        },
        "Griger's Base (Left)": {
            "Phase Upgrade Outside Griger's Base": 405,
        },
        "Mountain Fall": {
            "Lower Mountain Phase Upgrade": 406,
        },
        "Upper Mountain": {
            "Upper Mountain Phase Upgrade": 407,
        },
        "Orb A": {
            "Orb A": 408,
        },
        "Orb B": {
            "Orb B": 409,
        },
        "Orb C": {
            "Orb C": 410,
        },
        "Orb D": {
            "Orb D": 411,
        },
    },
}

OPTION_LOCATION_RULES: dict[str, dict[str, Rule]] = {
    "add_ambushes": {
        "Cottospark Ambush": (Has("Spin Dodge") & (Has("Charge Shot") | HasAll("Energy Claw", "Vile Claw"))),
        "Block Puzzle Ambush": (Has("Spin Dodge") & (Has("Charge Shot") | HasAll("Energy Claw", "Vile Claw"))),
        "Claw Bounce Ambush": (Has("Spin Dodge") & (Has("Charge Shot") | HasAll("Energy Claw", "Vile Claw"))),
    },
    "add_physical": {
        "Pre-Spin Dodge Health Upgrade": (Has("Charge Shot") | HasAll("Energy Claw", "Vile Claw")),
        "Phase Upgrade Outside Griger's Base": HasAny("Wall Run", "Spin Dodge"),
        "Orb A": (Has("Spin Dodge") | HasAll("Speed Boost", "Wall Run")),
        "Orb B": (Has("Spin Dodge") | CanReachEntrance("Upper Floatlands -> Orb B") | HasAll("Speed Boost", "Wall Run")),
        "Orb C": (Has("Wall Run") | HasAll("Spin Dodge", "Spin Double") | HasAll("Spin Dodge", "Twister Jump")),
    },
}

GOAL: Rule = Has("Victory")

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