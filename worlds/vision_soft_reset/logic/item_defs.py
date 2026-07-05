from functools import reduce
import dataclasses
from BaseClasses import ItemClassification
from .interpreter import LispState, LispSymbol

@dataclasses.dataclass
class ItemInfo:
    name: str
    id: int
    classification: str
    filler_weight: int | None = None
    trimmable: bool = False
    pool_option: str | None = None


def item(name: str, id: int, classifications: LispSymbol | list[LispSymbol], *,
         weight: int | None = None,
         trimmable: bool = False,
         pool_option: str | None = None) -> ItemInfo:
    if isinstance(classifications, list):
        classification = " | ".join([f"ItemClassification.{cl[:]}" for cl in classifications])
    else:
        classification = f"ItemClassification.{classifications[:]}"
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

def use() -> None:
    LispState.reset()
    LispState.register_global(item)
    LispState.register_global(item_list, "item-list")
