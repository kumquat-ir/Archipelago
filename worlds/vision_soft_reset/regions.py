# This file is generated, do not edit!
# Instead see templates/regions.template.py and logic/regions.lisp

from worlds.AutoWorld import World
from BaseClasses import Region
from rule_builder.rules import Rule, Has, HasAll, HasAny, OptionFilter, True_, CanReachRegion, CanReachEntrance
from .options import HardLogic

REGION_DATA: dict[str, dict[str, Rule | None] | None] = {
    "Ship": {
        "First Puzzle Solution": (Has("Charge Shot") | HasAll("Energy Claw", "Vile Claw")),
        "Past First Puzzle": None,
        "Left of Ship": HasAny("Wall Run", "Spin Dodge"),
        "Power Area": (Has("Charge Shot") | HasAll("Energy Claw", "Vile Claw")),
        "Above First Puzzle": ((Has("Charge Shot") | HasAll("Energy Claw", "Vile Claw")) | Has("Wall Run")),
        "After Griger": Has("Strip Suit"),
        "Mountain Water Run": HasAll("Speed Boost", "Wall Run"),
    },
    "First Puzzle Solution": {
        "Spin Dodge Area": (True_() & OptionFilter(HardLogic, True)),
    },
    "Past First Puzzle": {
        "Pre-Spin Dodge": (CanReachRegion("Power Area") | HasAny("Wall Run", "Spin Dodge")),
        "Griger's Base (Top)": ((CanReachRegion("Power Area") & Has("Spin Dodge")) | (Has("Energy Claw") | HasAll("Speed Boost", "Piercing Speed")) | HasAll("Spin Dodge", "Spin Double")),
        "Above Wall Run": (Has("Energy Claw") | HasAll("Speed Boost", "Piercing Speed")),
        "Endoplanetary Shield": (Has("Charge Shot") | HasAll("Energy Claw", "Vile Claw")),
    },
    "Above First Puzzle": {
        "Mountain Chamber": (HasAll("Wall Run", "Spin Dodge") | HasAll("Speed Boost", "Wall Run")),
    },
    "Power Area": {
        "Under Beach": HasAny("Wall Run", "Spin Dodge"),
        "After Griger": (Has("Energy Claw") | HasAll("Speed Boost", "Piercing Speed", "Engine Tune")),
    },
    "Pre-Spin Dodge": {
        "Spin Dodge Area": None,
    },
    "Spin Dodge Area": {
        "Pre-Spin Dodge": Has("Spin Dodge"),
        "First Puzzle Solution": Has("Spin Dodge"),
    },
    "Griger": {
        "After Griger": (Has("Energy Claw") | HasAll("Speed Boost", "Piercing Speed", "Engine Tune")),
        "Griger's Base (Top)": None,
    },
    "After Griger": {
        "Power Area": (Has("Energy Claw") | HasAll("Speed Boost", "Piercing Speed")),
        "Griger": Has("Energy Claw"),
    },
    "Claw Bounce Area": {
        "Orb A": HasAll("Spin Dodge", "Energy Claw"),
        "Griger's Base (Bottom Right)": (HasAny("Wall Run", "Spin Dodge") & Has("Energy Claw")),
        "Wall Run Area": ((Has("Charge Shot") | HasAll("Energy Claw", "Vile Claw")) & HasAny("Wall Run", "Spin Dodge")),
    },
    "Wall Run Area": {
        "Claw Bounce Area": HasAll("Wall Run", "Spin Dodge"),
        "Above Wall Run": HasAll("Wall Run", "Spin Dodge"),
    },
    "Above Wall Run": {
        "Past First Puzzle": (Has("Energy Claw") | HasAll("Speed Boost", "Piercing Speed")),
        "Wall Run Area": (HasAll("Wall Run", "Spin Dodge") | HasAll("Spin Dodge", "Spin Double")),
        "Griger's Base (Bottom Right)": ((HasAll("Wall Run", "Spin Dodge") | HasAll("Spin Dodge", "Spin Double")) & Has("Speed Boost")),
    },
    "Griger's Base (Top)": {
        "Griger's Base (Central)": None,
        "Griger": HasAny("Wall Run", "Spin Dodge"),
    },
    "Griger's Base (Central)": {
        "Griger's Base (Top)": Has("Spin Dodge"),
        "Griger's Base (Right)": (((Has("Charge Shot") | HasAll("Energy Claw", "Vile Claw")) & HasAny("Wall Run", "Spin Dodge")) | (Has("Energy Claw") | HasAll("Speed Boost", "Piercing Speed", "Engine Tune"))),
        "Griger's Base (Left)": ((Has("Spin Dodge") | (Has("Wall Run") & Has("Energy Claw"))) & (Has("Energy Claw") | HasAll("Speed Boost", "Piercing Speed"))),
        "Griger's Base (Bottom Right)": (HasAny("Wall Run", "Spin Dodge") & (((Has("Charge Shot") | HasAll("Energy Claw", "Vile Claw")) & HasAny("Wall Run", "Spin Dodge")) | (Has("Energy Claw") | HasAll("Speed Boost", "Piercing Speed")))),
        "Griger's Base (Bottom Left)": ((Has("Energy Claw") | HasAll("Speed Boost", "Piercing Speed", "Engine Tune")) | (((Has("Charge Shot") | HasAll("Energy Claw", "Vile Claw")) & HasAny("Wall Run", "Spin Dodge")) & (Has("Spin Dodge") & (Has("Charge Shot") | HasAll("Energy Claw", "Vile Claw"))))),
    },
    "Griger's Base (Right)": None,
    "Griger's Base (Left)": {
        "Griger's Base (Central)": (HasAny("Wall Run", "Spin Dodge") & Has("Energy Claw")),
        "Above Orb A": (Has("Energy Claw") & (HasAll("Wall Run", "Spin Dodge") | HasAll("Spin Dodge", "Spin Double"))),
    },
    "Griger's Base (Bottom Right)": {
        "Claw Bounce Area": HasAll("Energy Claw", "Spin Dodge"),
        "Griger's Base (Central)": (Has("Wall Run") & Has("Energy Claw")),
        "Griger's Base (Powerless Room)": (HasAny("Wall Run", "Spin Dodge") & (CanReachEntrance("After Griger -> Griger") | CanReachEntrance("Claw Bounce Area -> Griger's Base (Bottom Right)") | CanReachEntrance("Griger's Base (Left) -> Griger's Base (Central)") | CanReachEntrance("Above Wall Run -> Griger's Base (Bottom Right)") | (CanReachEntrance("Past First Puzzle -> Griger's Base (Top)") & ((Has("Energy Claw") | HasAll("Speed Boost", "Piercing Speed")) | HasAll("Spin Dodge", "Spin Double"))))),
    },
    "Griger's Base (Bottom Left)": {
        "Griger's Base (Central)": (Has("Wall Run") & Has("Energy Claw")),
        "Griger's Base (Powerless Room)": (HasAny("Wall Run", "Spin Dodge") & (CanReachEntrance("After Griger -> Griger") | CanReachEntrance("Claw Bounce Area -> Griger's Base (Bottom Right)") | CanReachEntrance("Griger's Base (Left) -> Griger's Base (Central)") | CanReachEntrance("Above Wall Run -> Griger's Base (Bottom Right)") | (CanReachEntrance("Past First Puzzle -> Griger's Base (Top)") & ((Has("Energy Claw") | HasAll("Speed Boost", "Piercing Speed")) | HasAll("Spin Dodge", "Spin Double"))))),
    },
    "Griger's Base (Powerless Room)": {
        "Griger's Base (Bottom Left)": None,
        "Griger's Base (Bottom Right)": HasAny("Wall Run", "Spin Dodge"),
    },
    "Left of Ship": {
        "Floatlands Entry": HasAll("Wall Run", "Spin Dodge"),
        "Beach": (Has("Energy Claw") | HasAll("Speed Boost", "Piercing Speed", "Engine Tune")),
    },
    "Under Beach": {
        "Beach": Has("Spin Dodge"),
        "Power Area": None,
        "Above Orb A": HasAll("Speed Boost", "Engine Tune"),
    },
    "Beach": {
        "Underwater": ((Has("Spin Dodge") & (Has("Charge Shot") | HasAll("Energy Claw", "Vile Claw"))) | Has("Strip Suit")),
    },
    "Underwater": {
        "Beach": Has("Strip Suit"),
        "Orb A": HasAny("Wall Run", "Spin Dodge"),
    },
    "Orb A": {
        "Underwater": None,
        "Claw Bounce Area": HasAll("Spin Dodge", "Energy Claw"),
        "Above Orb A": HasAll("Wall Run", "Spin Dodge"),
    },
    "Above Orb A": {
        "Orb A": None,
        "Griger's Base (Left)": Has("Wall Run"),
        "Under Beach": HasAll("Speed Boost", "Wall Run"),
    },
    "Endoplanetary Shield": {
        "Hot Water Area": (Has("Wall Run") & HasAny("Spin Dodge", "Speed Boost") & (HasAll("Heat Reisist", "Spin Dodge") | HasAll("Spin Dodge", "Spin Double"))),
        "Past First Puzzle": (HasAll("Speed Boost", "Wall Run") & (Has("Charge Shot") | HasAll("Energy Claw", "Vile Claw"))),
    },
    "Hot Water Area": {
        "Warehouse": (HasAll("Speed Boost", "Wall Run") & (HasAll("Heat Resist", "Spin Dodge") | HasAll("Spin Dodge", "Spin Double"))),
        "Endoplanetary Shield": Has("Wall Run"),
    },
    "Warehouse": {
        "Orb D": Has("Strip Suit"),
        "Hot Water Area": Has("Speed Boost"),
    },
    "Orb D": None,
    "Floatlands Entry": {
        "Upper Floatlands": (HasAll("Wall Run", "Spin Dodge") & (CanReachRegion("Power Area") | HasAll("Spin Dodge", "Spin Double"))),
        "Lower Floatlands": Has("Spin Dodge"),
        "Orb B": HasAll("Wall Run", "Spin Dodge"),
    },
    "Upper Floatlands": {
        "Orb B": None,
        "Floatlands Entry": None,
        "Right Floatlands": (Has("Spin Dodge") & HasAny("Energy Claw", "Spin Double", "Twister Jump")),
    },
    "Lower Floatlands": {
        "Orb B": HasAll("Wall Run", "Spin Dodge"),
    },
    "Orb B": {
        "Lower Floatlands": None,
        "Upper Floatlands": (HasAll("Wall Run", "Spin Dodge") & (HasAll("Spin Dodge", "Spin Double") | HasAll("Speed Boost", "Wall Run"))),
        "Floatlands Ambush": None,
        "Floatlands Entry": Has("Spin Dodge"),
    },
    "Floatlands Ambush": {
        "Right Floatlands": Has("Wall Run"),
        "Orb B": (Has("Wall Run") & HasAny("Spin Dodge", "Speed Boost")),
        "Lower Floatlands": HasAny("Spin Dodge", "Speed Boost"),
        "Floatlands Entry": Has("Spin Dodge"),
        "Solatia Run": Has("Speed Boost"),
    },
    "Right Floatlands": {
        "Floatlands Ambush": None,
        "Upper Floatlands": HasAny("Energy Claw", "Spin Dodge"),
        "Solatia": (((CanReachRegion("Upper Floatlands") & CanReachRegion("Lower Floatlands") & CanReachRegion("Floatlands Entry") & CanReachRegion("Power Area")) | HasAll("Speed Boost", "Engine Tune")) & HasAll("Wall Run", "Spin Dodge")),
    },
    "Solatia": {
        "Solatia Run": None,
    },
    "Solatia Run": {
        "Floatlands Ambush": Has("Speed Boost"),
        "Upper Mountain": HasAll("Speed Boost", "Wall Run"),
    },
    "Upper Mountain": {
        "Solatia Run": Has("Speed Boost"),
        "Mountain Chamber": None,
        "Mountain Fall": None,
        "Mountaintop": (HasAll("Wall Run", "Spin Dodge") & (CanReachEntrance("Warehouse -> Hot Water Area") & CanReachEntrance("Hot Water Area -> Endoplanetary Shield") & CanReachEntrance("Endoplanetary Shield -> Past First Puzzle")) & CanReachRegion("Orb A") & CanReachRegion("Orb B") & CanReachRegion("Orb C") & CanReachRegion("Orb D")),
    },
    "Mountain Chamber": {
        "Upper Mountain": HasAll("Wall Run", "Spin Dodge"),
        "Mountain Water Run": None,
        "Above First Puzzle": None,
        "Orb C": (Has("Strip Suit") | (OptionFilter(HardLogic, True) & HasAll("Wall Run", "Spin Dodge") & HasAll("Spin Dodge", "Spin Double"))),
    },
    "Mountain Water Run": {
        "Mountain Chamber": (HasAll("Wall Run", "Spin Dodge") | HasAll("Speed Boost", "Wall Run")),
    },
    "Orb C": {
        "Mountain Water Run": Has("Wall Run"),
        "Mountain Fall": HasAny("Wall Run", "Spin Dodge"),
    },
    "Mountain Fall": {
        "Warehouse": Has("Strip Suit"),
        "Orb C": None,
        "Upper Mountain": HasAll("Wall Run", "Spin Dodge"),
    },
    "Mountaintop": None,
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