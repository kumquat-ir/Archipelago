from typing import Optional, Any
import itertools
import json
import os
import re

from ..locations import LocationData, AccessInfo
from ..types.condition import *
from ..types.regions import RegionsData, RegionConnection
from .lists import ListInfo

# manual mapping, these are not named in a way where they can be cleanly matched
_HOSTED_QUEST_NAMES: dict[str, str] = {
    "Round and Round": "AR-parkour",
    "Bergen Trailblazing": "BT-TB-done",
    "Bergen Trailblazing Collect": "BT-TB-collect",
    "Bergen Trailblazing Defeat": "BT-TB-defeat",
    "Bergen Trailblazing Landmarks": "BT-TB-poi",
    "Bergen Trailblazing Data Probe": "BT-TB-probe",
    "The Legendary Bunny": "BT-bunny",
    "Trial of Aspiration": "BV-asp-trial",
    "Challenge of Aspiration": "BV-asp-challenge",
    "Trial of Progression": "BV-prog-trial",
    "Challenge of Progression": "BV-prog-challenge",
    "Filthy Frobbits": "BV-frobbits",
    "Explosive Debugging": "BV-EX-mine",
    "Kidding Around": "BV-kidding",
    "Fancy Tophat": "BV-hat",
    "Building a Base": "BV-omni-build",
    "First Steps": "AR-first",
    "A Promise is a Promise": "dkar1",
    "A Promise is a Promise 2": "dkar2",
    "A Promise is a Promise 3": "dkar3",
    "A Promise is a Promise 4": "dkar4",
    "A Promise is a Promise 5": "dkar5",
    "Autumn's Rise Trailblazing": "AR-TB-done",
    "Autumn's Rise Collect": "AR-TB-collect",
    "Autumn's Rise Defeat": "AR-TB-defeat",
    "Autumn's Rise Landmarks": "AR-TB-poi",
    "Autumn's Rise Data Probe": "AR-TB-probe",
    "Maroon Valley Trailblazing": "MV-TB-done",
    "Maroon Valley Collect": "MV-TB-collect",
    "Maroon Valley Defeat": "MV-TB-defeat",
    "Maroon Valley Landmarks": "MV-TB-poi",
    "Maroon Valley Data Probe": "MV-TB-probe",
    "Gaia's Garden Trailblazing": "GG-TB-done",
    "Gaia's Garden Collect": "GG-TB-collect",
    "Gaia's Garden Defeat": "GG-TB-defeat",
    "Gaia's Garden Landmarks": "GG-TB-poi",
    "Gaia's Garden Data Probe": "GG-TB-probe",
    "Turret Defense": "GG-turret-1",
    "An Original Idea": "GG-turret-2",
    "Small Time Delivery": "RH-delivery",
    "Digging for Data": "RH-data-digging",
    "It Can Dig But It Can't Hide": "RH-hillkat",
    "Sickly Trees": "RH-tree-1",
    "Intensive Tree Care": "RH-tree-2",
    "Petty Crime Hunter": "RH-petty",
    "Smuggle Trouble": "RH-smuggle-1",
    "Wood 'n' Steaks": "RH-steaks-1",
    "Meating Expectations": "RH-steaks-2",
    "Training: VRP": "RH-vrp",
    "Training: VPI": "RH-vpi",
    "Blasting Shells": "MV-blasting",
    "Crate Hate": "MV-crate",
    "Melting this Cold Fiend": "GG-snowman",
    "Lakeside Escort": "GG-escort",
    "Rooting for Power": "GG-rooting",
    "Talatu Introductions": "botanics-1",
    "Talatu Bergen 25%": "botanics-2",
    "Talatu Ba'kii 50%": "botanics-3",
    "Talatu Basin 75%": "botanics-4",
}

class TrackerData:
    location_name_mapping: dict[str, dict[str, dict[str, LocationData]]]
    item_name_mapping: dict[str, str]
    quest_name_mapping: dict[str, str]
    tracker_dir: str
    lists: ListInfo
    regions: dict[str, RegionsData]

    def __init__(self, tracker_dir: str, lists: ListInfo, regions: dict[str, RegionsData]):
        self.tracker_dir = tracker_dir
        self.location_name_mapping = {}
        self.item_name_mapping = {}
        self.quest_name_mapping = {}
        self.lists = lists
        self.regions = regions

        self._get_data_mappings()

    def _set_location_mapping(self, region: str, location: str, section: str, value: LocationData):
        self.location_name_mapping.setdefault(region, {}).setdefault(location, {})[section] = value

    def _get_data_mappings(self):
        tracker_id_mapping = {}
        with open(os.path.join(self.tracker_dir, "scripts", "autotracking", "location_mapping.lua")) as f:
            for line in f.readlines():
                match = re.search(r"\[(\d+)\].*\"@(.*)/(.*)/(.*)\"", line)
                if match is None:
                    continue
                tracker_id_mapping[int(match[1])] = match.groups()[1:]

        for location in self.lists.locations_data.values():
            if location.code in tracker_id_mapping:
                tracker_path = tracker_id_mapping[location.code]
                self._set_location_mapping(tracker_path[0], tracker_path[1].replace("\\n", "\n"), tracker_path[2], location)

        self._set_location_mapping("Vermillion Wasteland", "Vermillion Wasteland - Vermillion Tower", "The Creator",
                                   LocationData("", None, AccessInfo({}, cond=[OrCondition([])])))
        self._set_location_mapping("Ku'lero Temple", "Ku'lero Temple U8 - The Rise", "Di'orbis",
                                   LocationData("", None, AccessInfo({}, cond=[OrCondition([])])))
        for mode, region_pack in self.regions.items():
            if "creator" in region_pack.goals:
                goal = region_pack.goals["creator"]
                loc_access = self.location_name_mapping["Vermillion Wasteland"]["Vermillion Wasteland - Vermillion Tower"]["The Creator"].access
                loc_access.region[mode] = goal.region
                loc_access.cond[0].subconditions.append(AndCondition([RegionCondition(mode, goal.region)] + (goal.condition or []))) #type:ignore
            if "diorbis" in region_pack.goals:
                goal = region_pack.goals["diorbis"]
                loc_access = self.location_name_mapping["Ku'lero Temple"]["Ku'lero Temple U8 - The Rise"]["Di'orbis"].access
                loc_access.region[mode] = goal.region
                loc_access.cond[0].subconditions.append(AndCondition([RegionCondition(mode, goal.region)] + (goal.condition or []))) #type:ignore

        tracker_id_mapping = {}
        with open(os.path.join(self.tracker_dir, "scripts", "autotracking", "item_mapping.lua")) as f:
            for line in f.readlines():
                match = re.search(r"\[(\d+)\].*\"(.*)\", \"", line)
                if match is None:
                    continue
                tracker_id_mapping[int(match[1])] = match[2]

        for item in self.lists.items_dict.values():
            if item.combo_id in tracker_id_mapping:
                self.item_name_mapping[item.item.name] = tracker_id_mapping[item.combo_id]

        with open(os.path.join(self.tracker_dir, "items", "hosted_quests.json")) as f:
            quest_data = json.load(f)
        for quest in quest_data:
            self.quest_name_mapping[quest["name"]
                                    .removesuffix(" Host")
                                    .removeprefix("AR ")
                                    .removeprefix("BT ")
                                    .removeprefix("BV ")
                                    .removeprefix("MV ")
                                    .removeprefix("RH ")
                                    .removeprefix("GG ")
                                    ] = quest["codes"]
        self.quest_name_mapping.update(_HOSTED_QUEST_NAMES)

    def _canonicalize(self, s: str) -> str:
        if s in self.item_name_mapping:
            return self.item_name_mapping[s]
        elif s in self.quest_name_mapping:
            return self.quest_name_mapping[s]
        if s not in ["Bronze Mail"] and not s.startswith("setting"):
            # ignoring bronze mail for now since it isn't implemented in the tracker
            # also ignore tracker settings since we won't have any mappings for them
            raise ValueError(f"Unknown name: {s}")
        return (s[0].lower() + s[1:]).replace(" ", "").replace("'", "")

    def _map_condition(self, cond: Condition, loc: Optional[int]) -> str:
        if isinstance(cond, OrCondition) or isinstance(cond, AndCondition) or isinstance(cond, NeverCondition):
            raise TypeError(f"Tried to map a boolean condition {cond}!")
        elif isinstance(cond, ItemCondition):
            return f"{self._canonicalize(cond.item_name)}{':' + str(cond.amount) if cond.amount != 1 else ""}"
        elif isinstance(cond, QuestCondition):
            return f"{self._canonicalize(cond.quest_name)}"
        elif isinstance(cond, LocationCondition):
            return f"{self._canonicalize(cond.location_name)}"
        elif isinstance(cond, RegionCondition):
            return f"@REGION/{cond.target_mode}/{cond.region_name}"
        elif isinstance(cond, AnyElementCondition):
            return f"$anyElement"
        elif isinstance(cond, VariableCondition):
            return f"$var|{cond.name}"
        elif isinstance(cond, VariableEntryCondition):
            return f"$vareq|{cond.name}|{cond.value}|{cond.desired}"
        elif isinstance(cond, ChestKeyCondition):
            return f"$newLock|{loc}{'|' + self._canonicalize(ChestKeyCondition.clearance_items[cond.default_level]) if cond.default_level != 'Default' else ''}"
        elif isinstance(cond, ShopSlotCondition):
            raise TypeError("Shop slot condition survived resolution!")
        elif isinstance(cond, BotanicsCompletionCondition):
            return f"$botanics|{cond.amount}"
        raise TypeError("Unknown condition type!")

    def _resolve_condition(self, cond: Condition):
        if isinstance(cond, ShopSlotCondition):
            return OrCondition([
                AndCondition([ItemCondition("settingShopReceiveSlots"), ItemCondition(self.lists.shop_unlock_by_shop_and_id[(cond.shop_name, cond.item_id)].item.name)]),
                AndCondition([ItemCondition("settingShopReceiveTypes"), ItemCondition(self.lists.shop_unlock_by_id[cond.item_id].item.name)]),
                AndCondition([ItemCondition("settingShopReceiveShops"), ItemCondition(self.lists.shop_unlock_by_shop[cond.shop_name].item.name)]),
                ItemCondition("settingShopReceiveOff"),
            ])
        elif isinstance(cond, RegionCondition) and cond.region_name in self.lists.shop_data:
            regions = self.lists.shop_data[cond.region_name].access.region
            return self._traverse_and_condition(AndCondition([
                OrCondition([RegionCondition(mode, region) for mode, region in regions.items()])
            ] + (self.lists.shop_data[cond.region_name].access.cond or [])))
        return cond

    def _traverse_and_condition(self, cond: AndCondition) -> AndCondition | OrCondition:
        result_conditions = []
        found_ors = []
        for subcond in cond.subconditions:
            subcond = self._resolve_condition(subcond)
            if isinstance(subcond, NeverCondition):
                continue
            elif isinstance(subcond, OrCondition):
                found_ors.append(self._traverse_or_condition(subcond))
            elif isinstance(subcond, AndCondition):
                result_conditions.extend(self._traverse_and_condition(subcond).subconditions)
            else:
                result_conditions.append(subcond)

        if len(found_ors) == 0:
            return AndCondition(result_conditions)

        result_subconditions = []
        for combo in itertools.product(*[orcond.subconditions for orcond in found_ors]):
            result_subconditions.append(self._traverse_and_condition(AndCondition(result_conditions + list(combo))))
        return self._traverse_or_condition(OrCondition(result_subconditions))

    def _traverse_or_condition(self, cond: OrCondition) -> OrCondition:
        result_conditions = []
        for subcond in cond.subconditions:
            subcond = self._resolve_condition(subcond)
            if isinstance(subcond, NeverCondition):
                continue
            elif isinstance(subcond, OrCondition):
                result_conditions.extend(self._traverse_or_condition(subcond).subconditions)
            elif isinstance(subcond, AndCondition):
                result_conditions.append(self._traverse_and_condition(subcond))
            else:
                result_conditions.append(subcond)
        return OrCondition(result_conditions)

    def _dnf_condition(self, raw: list[Condition], loc: Optional[int] = None) -> list[str]:
        result = []
        cond = self._traverse_and_condition(AndCondition(raw))

        if isinstance(cond, AndCondition):
            cond = OrCondition([cond])

        for subcond in cond.subconditions:
            if isinstance(subcond, AndCondition):
                cond_strs = [self._map_condition(c, loc) for c in subcond.subconditions]
            else:
                cond_strs = [self._map_condition(subcond, loc)]
            result.append(", ".join(list(dict.fromkeys(cond_strs))))

        if len(result) == 0:
            result.append("")

        return result

    def update_locations(self, file):
        print(file)
        with open(os.path.join(self.tracker_dir, "locations", file)) as opened_file:
            data = json.load(opened_file)

        for location_root in data:
            if "name" not in location_root:
                continue
            root_name = location_root["name"]

            for location in location_root.get("children", []):
                if "name" not in location:
                    continue
                location_name = location["name"]

                for section in location.get("sections", []):
                    if "name" not in section:
                        continue
                    section_name = section["name"]
                    location_data = self.location_name_mapping[root_name][location_name].get(section_name, None)

                    if location_data is None:
                        # shop item types don't have an associated location id, but have the same logic as their slot counterpart
                        section_name = section_name.replace(" Type ", " Slot ")
                        location_data = self.location_name_mapping[root_name][location_name].get(section_name, None)

                        if location_data is None:
                            raise NameError(f"no location data for @{root_name}/{location_name}/{section_name}!! fix this")

                    regions = []
                    shop_region = None
                    for mode, region in location_data.access.region.items():
                        if region not in self.lists.shop_data:
                            regions.append((mode, region))
                        else:
                            shop_region = region

                    section_logic = location_data.access.cond or []
                    if shop_region is not None:
                        section_logic.extend(self.lists.shop_data[shop_region].access.cond or [])
                        regions = list(self.lists.shop_data[shop_region].access.region.items())
                    location_cond = self._dnf_condition([OrCondition([RegionCondition(mode, region) for mode, region in regions])])
                    section_cond = self._dnf_condition(section_logic, location_data.code)

                    location["access_rules"] = location_cond
                    section["access_rules"] = section_cond

        with open(os.path.join(self.tracker_dir, "locations", file), "w") as opened_file:
            json.dump(data, opened_file, indent=4)

    def _base_region_condition(self, mode: str) -> str:
        match mode:
            case "linear":
                return "settingOpenModeClosed"
            case "open":
                return "settingOpenModeOpen"
            case _:
                raise ValueError(f"Unknown region mode {mode}!")

    def generate_regions(self):
        region_data = []

        for mode, region_pack in self.regions.items():
            mode_data: dict[str, Any] = {}

            seen_regions = set()
            no_logic_regions = []
            for connection in region_pack.region_connections:
                if connection.region_from in region_pack.excluded_regions or connection.region_to in region_pack.excluded_regions:
                    continue

                if connection.region_from not in seen_regions:
                    no_logic_regions.append(connection.region_from)

                seen_regions.add(connection.region_from)
                seen_regions.add(connection.region_to)

                if connection.region_to in no_logic_regions:
                    no_logic_regions.remove(connection.region_to)

                mode_data.setdefault(connection.region_to, {
                    "name": connection.region_to,
                    "access_rules": []
                })["access_rules"].extend(self._dnf_condition([RegionCondition(mode, connection.region_from)] + (connection.cond or [])))

            for region in no_logic_regions + ["Menu"]:
                if region in region_pack.excluded_regions:
                    continue

                if region not in mode_data:
                    mode_data[region] = {
                        "name": region,
                        "access_rules": [self._base_region_condition(mode)]
                    }

            region_data.append({
                "name": mode,
                "children": list(mode_data.values())
            })

        with open(os.path.join(self.tracker_dir, "locations", "regions_generated.json"), "w") as opened_file:
            json.dump([{
                "name": "REGION",
                "children": region_data
            }], opened_file, indent=4)
