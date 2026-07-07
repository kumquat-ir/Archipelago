from typing import Any
from collections.abc import Mapping
from . import items, regions, locations, options
from worlds.AutoWorld import World, WebWorld

class VisionSoftResetWebWorld(WebWorld):
    game = "Vision Soft Reset"
    option_groups = options.option_groups

class VisionSoftResetWorld(World):
    """
    Peer into the future in this time-travelling metroidvania. Run, jump, shoot
    and more through varied environments as a clairvoyant cyborg on a mission to
    prevent a looming planetary disaster. It's a classic 2D action-adventure
    revamped with modern sensibilities and a plethora of new mechanics.
    """

    game = "Vision Soft Reset"

    web = VisionSoftResetWebWorld()

    options_dataclass = options.VisionSoftResetOptions
    options: options.VisionSoftResetOptions

    item_name_to_id = items.ITEM_ID_MAP
    location_name_to_id = locations.LOCATION_ID_MAP

    origin_region_name = "Ship"

    # no idea if this is necessary for not, but this is a small world so it should be fine
    explicit_indirect_conditions = False

    def create_regions(self) -> None:
        regions.create_regions(self)
        regions.connect_regions(self)
        locations.create_locations(self)

    def set_rules(self) -> None:
        locations.set_rules(self)

    def create_items(self) -> None:
        items.fill_item_pool(self)


    def create_item(self, name: str) -> items.VSRItem:
        return items.create_item(self, name)

    def get_filler_item_name(self) -> str:
        return items.random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return {}
