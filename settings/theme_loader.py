import subprocess
import sys
import json
from path import qtile_path
from os import listdir
from os.path import isfile, join


def dict_enum(l: list) -> dict:
    return {i: l[i] for i in range(len(l))}


def list_themes():
    settings_path = join(qtile_path, 'settings')
    themes_path = join(settings_path, 'themes')
    themes_list = [f for f in listdir(themes_path) if f.endswith('.json')]
    themes_dict = dict_enum(themes_list)

    for i in themes_dict:
        print(f'{i}: {themes_dict[i][:-5]}')
    selection = themes_dict[int(input('Select a theme to be aplied: '))]

    def_path = join(settings_path, 'default_globals.json')
    with open(def_path, 'r') as f:
        def_file = json.load(f)

    def_file["colors"] = selection
    with open(def_path, 'w') as f:
        f.write(json.dumps(def_file, indent=4))


list_themes()
