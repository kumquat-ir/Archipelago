import dataclasses
from .interpreter import LispState, LispSymbol

def noop(*_args, **_kwargs): pass

def noop_names(*names) -> None:
    for name in names:
        LispState.register_global(noop, name)

@dataclasses.dataclass
class ItemInfo:
    name: str
    id: int
    decryptor_id: str | None = None
    card_id: int | None = None
    phase_amount: int | None = None

@dataclasses.dataclass
class LocationInfo:
    name: str
    id: int
    decryptor_id: str | None = None
    card_id: int | None = None
    ambush_coords: list[int] | None = None
    health_upgrade_id: str | None = None
    phase_upgrade_id: str | None = None
    orb_id: str | None = None

def item(name: str, id: int, *_args, decryptor_id: str | None = None, card_id: int | None = None, phase_amount: int | None = None, **_kwargs) -> ItemInfo:
    return ItemInfo(name, id, decryptor_id, card_id, phase_amount)

def item_list(*items: ItemInfo) -> tuple[dict[int, str], dict[int, int], dict[int, int]]:
    decryptor_ids: dict[int, str] = {}
    card_ids: dict[int, int] = {}
    phase_refills: dict[int, int] = {}

    for item in items:
        if item.decryptor_id is not None:
            decryptor_ids[item.id] = item.decryptor_id
        elif item.card_id is not None:
            card_ids[item.id] = item.card_id
        elif item.phase_amount is not None:
            phase_refills[item.id] = item.phase_amount

    return (decryptor_ids, card_ids, phase_refills)

def location(name: str, id: int, *_args,
             decryptor_id: str | None = None,
             card_id: int | None = None,
             ambush_coords: list[int] | None = None,
             health_upgrade_id: str | None = None,
             phase_upgrade_id: str | None = None,
             orb_id: str | None = None,
             **_kwargs) -> LocationInfo:
    return LocationInfo(name, id, decryptor_id, card_id, ambush_coords, health_upgrade_id, phase_upgrade_id, orb_id)

def location_list(*locations: LocationInfo | None) -> tuple[dict[str, int], dict[int, int], dict[tuple[int, int], int], dict[str, int], dict[str, int], dict[str, int]]:
    decryptor_ids: dict[str, int] = {}
    card_ids: dict[int, int] = {}
    ambush_locations: dict[tuple[int, int], int] = {}
    health_locations: dict[str, int] = {}
    phase_locations: dict[str, int] = {}
    orb_locations: dict[str, int] = {}

    for location in locations:
        if location is None: continue # events are None here since they aren't real
        if location.decryptor_id is not None:
            decryptor_ids[location.decryptor_id] = location.id
        elif location.card_id is not None:
            card_ids[location.card_id] = location.id
        elif location.ambush_coords is not None:
            ambush_locations[(location.ambush_coords[0], location.ambush_coords[1])] = location.id
        elif location.health_upgrade_id is not None:
            health_locations[location.health_upgrade_id] = location.id
        elif location.phase_upgrade_id is not None:
            phase_locations[location.phase_upgrade_id] = location.id
        elif location.orb_id is not None:
            orb_locations[location.orb_id] = location.id

    return (decryptor_ids, card_ids, ambush_locations, health_locations, phase_locations, orb_locations)

def logic_data(locations, **_kwargs):
    return locations

def use() -> None:
    LispState.reset()
    noop_names("if-option", "items", "any-item", "region?", "entrance?", "and", "or", "true", "option", "->", "region", "region-list", "event")
    LispState.register_global(item)
    LispState.register_global(item_list, "item-list")
    LispState.register_global(location)
    LispState.register_global(location_list, "location-list")
    LispState.register_global(logic_data, "logic-data")
