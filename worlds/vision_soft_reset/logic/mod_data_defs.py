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

@dataclasses.dataclass
class LocationInfo:
    name: str
    id: int
    decryptor_id: str | None = None
    card_id: int | None = None

def item(name: str, id: int, *_args, decryptor_id: str | None = None, card_id: int | None = None, **_kwargs) -> ItemInfo:
    return ItemInfo(name, id, decryptor_id, card_id)

def item_list(*items: ItemInfo) -> tuple[dict[int, str], dict[int, int]]:
    decryptor_ids: dict[int, str] = {}
    card_ids: dict[int, int] = {}

    for item in items:
        if item.decryptor_id is not None:
            decryptor_ids[item.id] = item.decryptor_id
        elif item.card_id is not None:
            card_ids[item.id] = item.card_id

    return (decryptor_ids, card_ids)

def location(name: str, id: int, *_args, decryptor_id: str | None = None, card_id: int | None = None, **_kwargs) -> LocationInfo:
    return LocationInfo(name, id, decryptor_id, card_id)

def location_list(*locations: LocationInfo) -> tuple[dict[str, int], dict[int, int]]:
    decryptor_ids: dict[str, int] = {}
    card_ids: dict[int, int] = {}

    for location in locations:
        if location is None: continue
        if location.decryptor_id is not None:
            decryptor_ids[location.decryptor_id] = location.id
        elif location.card_id is not None:
            card_ids[location.card_id] = location.id

    return (decryptor_ids, card_ids)

def logic_data(locations, **_kwargs):
    return locations

def use() -> None:
    LispState.reset()
    noop_names("items", "any-item", "region?", "entrance?", "and", "or", "true", "option", "->", "region", "region-list", "event")
    LispState.register_global(item)
    LispState.register_global(item_list, "item-list")
    LispState.register_global(location)
    LispState.register_global(location_list, "location-list")
    LispState.register_global(logic_data, "logic-data")
