# This file is generated, do not edit!
# Instead see templates/ut_data.template.py and logic/locations.lisp

UT_NAME_MAPPING = {
{%- for name, id in ut_mapping.items() %}
    "{{ name }}": {{ id }},
{%- endfor %}
}

tracker_world = {
    "external_pack_key": "ut_pack_path",
    "map_page_maps": "maps/maps.json",
    "map_page_locations": "locations/locations.json",
    "poptracker_name_mapping": UT_NAME_MAPPING
}
