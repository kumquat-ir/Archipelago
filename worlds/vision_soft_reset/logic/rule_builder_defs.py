from typing import Any
import dataclasses
from .interpreter import LispState, LispSymbol

@dataclasses.dataclass
class RegionInfo:
    name: str
    connections: dict[str, str | None]

@dataclasses.dataclass
class LocationInfo:
    name: str
    id: int | None
    region: str
    condition: str | None
    event_item: str | None

def item(*names: str) -> str:
    if len(names) == 1:
        return f'Has("{names[0]}")'
    return f"HasAll({", ".join(['"' + name + '"' for name in names])})"

def any_item(*names: str) -> str:
    return f"HasAny({", ".join(['"' + name + '"' for name in names])})"

def region_access(name: str) -> str:
    return f'CanReachRegion("{name}")'

def entrance_access(from_region: str, to_region: str) -> str:
    return f'CanReachEntrance("{from_region} -> {to_region}")'

def _and(*args: str) -> str:
    return f"({" & ".join(args)})"

def _or(*args: str) -> str:
    return f"({" | ".join(args)})"

def _true() -> str:
    return "True_()"

def option(option: LispSymbol, value: Any) -> str:
    return f"OptionFilter({option[:]}, {value})"

def connection(to: str, condition: str | None = None) -> tuple[str, str | None]:
    return (to, condition)

def region(name: str, *connections: tuple[str, str | None]) -> RegionInfo:
    return RegionInfo(name, dict(connections))

def region_list(*regions: RegionInfo) -> dict[str, dict[str, str | None]]:
    return {region.name: region.connections for region in regions}

def location(name: str, id: int, region: str, condition: str | None = None) -> LocationInfo:
    return LocationInfo(name, id, region, condition, None)

def event(location_name: str, item_name: str, region: str, condition: str | None = None) -> LocationInfo:
    return LocationInfo(location_name, None, region, condition, item_name)

def location_list(*locations: LocationInfo) -> tuple[dict[str, int], dict[str, dict[str, int | str]], dict[str, str], dict[str, dict[str, str]]]:
    id_mapping: dict[str, int] = {}
    region_mapping: dict[str, dict[str, int | str]] = {}
    rules: dict[str, str] = {}
    events: dict[str, dict[str, str]] = {}

    for location in locations:
        if location.id is not None:
            id_mapping[location.name] = location.id
            if location.region not in region_mapping:
                region_mapping[location.region] = {}
            region_mapping[location.region][location.name] = location.id
        else:
            assert location.event_item is not None
            if location.region not in events:
                events[location.region] = {}
            events[location.region][location.name] = location.event_item
        if location.condition is not None:
            rules[location.name] = location.condition

    return (id_mapping, region_mapping, rules, events)

# type soup
def logic_data(regions, locations, goal) -> tuple[dict[str, dict[str, str | None]], tuple[dict[str, int], dict[str, dict[str, int | None]], dict[str, str], dict[str, dict[str, str]]], str]:
    return (regions, locations, goal)

def use() -> None:
    LispState.reset()
    LispState.register_global(item)
    LispState.register_global(any_item, "any-item")
    LispState.register_global(region_access, "region?")
    LispState.register_global(entrance_access, "entrance?")
    LispState.register_global(_and, "and")
    LispState.register_global(_or, "or")
    LispState.register_global(_true, "true")
    LispState.register_global(option)
    LispState.register_global(connection, "->")
    LispState.register_global(region)
    LispState.register_global(region_list, "region-list")
    LispState.register_global(location)
    LispState.register_global(event)
    LispState.register_global(location_list, "location-list")
    LispState.register_global(logic_data, "logic-data")
