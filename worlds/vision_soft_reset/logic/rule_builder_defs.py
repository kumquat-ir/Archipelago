from typing import Any
import dataclasses
from BaseClasses import ItemClassification
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
    include_option: str | None

@dataclasses.dataclass
class ItemInfo:
    name: str
    id: int
    classification: str
    filler_weight: int | None = None
    trimmable: bool = False
    pool_option: str | None = None

def if_option(cond: str, t: LispSymbol, f: LispSymbol) -> str:
    return f'lambda world: ItemClassification.{t[:]} if getattr(world.options, "{cond}").value else ItemClassification.{f[:]}'

def item(name: str, id: int, classifications: LispSymbol | list[LispSymbol] | str, *,
         weight: int | None = None,
         trimmable: bool = False,
         pool_option: str | None = None, **_kwargs) -> ItemInfo:
    if isinstance(classifications, list):
        classification = " | ".join([f"ItemClassification.{cl[:]}" for cl in classifications])
    elif isinstance(classifications, LispSymbol):
        classification = f"ItemClassification.{classifications[:]}"
    else:
        classification = classifications
    return ItemInfo(name, id, classification, weight, trimmable, pool_option)

def item_list(*items: ItemInfo) -> tuple[dict[str, int], dict[str, str], dict[str, int], list[str], list[str], dict[str, list[str]]]:
    id_mapping: dict[str, int] = {}
    classification_mapping: dict[str, str] = {}
    filler_weights: dict[str, int] = {}
    normal_pool: list[str] = []
    trimmable: list[str] = []
    option_pools: dict[str, list[str]] = {}

    for item in items:
        id_mapping[item.name] = item.id
        classification_mapping[item.name] = item.classification

        if item.filler_weight is not None:
            filler_weights[item.name] = item.filler_weight
        elif item.pool_option is not None:
            if item.pool_option not in option_pools:
                option_pools[item.pool_option] = []
            option_pools[item.pool_option].append(item.name)
        else:
            normal_pool.append(item.name)

        if item.trimmable:
            trimmable.append(item.name)

    return (id_mapping, classification_mapping, filler_weights, normal_pool, trimmable, option_pools)

def items(*names: str) -> str:
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

def location(name: str, id: int, region: str, condition: str | None = None, include_option: str | None = None, **_kwargs) -> LocationInfo:
    return LocationInfo(name, id, region, condition, None, include_option)

def event(location_name: str, item_name: str, region: str, condition: str | None = None) -> LocationInfo:
    return LocationInfo(location_name, None, region, condition, item_name, None)

def location_list(*locations: LocationInfo):
    id_mapping: dict[str, int] = {}
    region_mapping: dict[str, dict[str, int | str]] = {}
    rules: dict[str, str] = {}
    events: dict[str, dict[str, str]] = {}
    option_region_mapping: dict[str, dict[str, dict[str, int | str]]] = {}
    option_rules: dict[str, dict[str, str]] = {}

    for location in locations:

        if location.id is not None:
            id_mapping[location.name] = location.id
            if location.include_option is not None:
                if location.include_option not in option_region_mapping:
                    option_region_mapping[location.include_option] = {}
                if location.region not in option_region_mapping[location.include_option]:
                    option_region_mapping[location.include_option][location.region] = {}
                option_region_mapping[location.include_option][location.region][location.name] = location.id
            else:
                if location.region not in region_mapping:
                    region_mapping[location.region] = {}
                region_mapping[location.region][location.name] = location.id
        else:
            assert location.event_item is not None
            if location.region not in events:
                events[location.region] = {}
            events[location.region][location.name] = location.event_item
        if location.condition is not None:
            if location.include_option is not None:
                if location.include_option not in option_rules:
                    option_rules[location.include_option] = {}
                option_rules[location.include_option][location.name] = location.condition
            else:
                rules[location.name] = location.condition

    return (id_mapping, region_mapping, rules, events, option_region_mapping, option_rules)

def logic_data(regions, locations, goal):
    return (regions, locations, goal)

def use() -> None:
    LispState.reset()
    LispState.register_global(if_option, "if-option")
    LispState.register_global(item)
    LispState.register_global(item_list, "item-list")
    LispState.register_global(items)
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
