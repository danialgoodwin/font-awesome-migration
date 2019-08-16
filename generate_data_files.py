#!/usr/bin/env python3
"""
Using metadata/icons.json from fontawesome.com, generate simplified versions of it.
"""

import json

# Input file
ICONS_FILE = 'res/icons.json'

# Output files
ICONS_V5_ONLY_BRAND_FILE = 'generated/icons-v5-only-brand.txt'  # Aka, prefix is fab
ICONS_V5_ONLY_REGULAR_FILE = 'generated/icons-v5-only-regular.txt'  # Aka, font-weight: normal, prefix is far
ICONS_V5_ONLY_SOLID_FILE = 'generated/icons-v5-only-solid.txt'  # Aka, font-weight: bold, prefix is fas

V5_UNICODE_NAME_ONLY_SOLID_FILE = 'generated/v5-unicode-name-only-solid.txt'  # Aka, font-weight: bold, prefix is fas


def output_to_file(file_name: str, contents):
    print('output_to_file({}, {})'.format(file_name, contents))
    with open(file_name, 'w') as f:
        for i in contents:
            if isinstance(i, tuple):
                f.write(' '.join(i))
            else:
                f.write(i)
            f.write('\n')
    print('Lines:', len(contents))
    print()


def generate_data_files(icons_file_path):
    print('generate_data_files({})'.format(icons_file_path))
    with open(icons_file_path) as f:
        icons_json = json.load(f)
    print('Total # of icons:', len(icons_json))

    only_brand_icons = []
    only_regular_icons = []
    only_solid_icons = []
    only_solid_unicode_name = []
    for icon_name, icon_json in icons_json.items():
        icon_unicode = icon_json['unicode']
        if 'styles' in icon_json:
            icon_styles = icon_json['styles']
            if len(icon_styles) == 1:
                style = icon_styles[0]
                if style == 'brands': only_brand_icons.append((icon_name, icon_unicode))
                elif style == 'regular': only_regular_icons.append((icon_name, icon_unicode))
                elif style == 'solid':
                    only_solid_icons.append((icon_name, icon_unicode))
                    only_solid_unicode_name.append((icon_unicode, icon_name))
        else:
            print('WARNING: No styles for icon:', icon_name)

    output_to_file(ICONS_V5_ONLY_BRAND_FILE, only_brand_icons)
    output_to_file(ICONS_V5_ONLY_REGULAR_FILE, only_regular_icons)
    output_to_file(ICONS_V5_ONLY_SOLID_FILE, only_solid_icons)

    v5_icons = sorted(only_solid_unicode_name, key=lambda x: x[0])
    output_to_file(V5_UNICODE_NAME_ONLY_SOLID_FILE, v5_icons)


generate_data_files(ICONS_FILE)
