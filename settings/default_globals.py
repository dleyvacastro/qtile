# Import Color Scheme
from os.path import isfile, join
from os import listdir
import json
import sys
# from settings.themes import nord as colors
from settings.path import qtile_path
# from settings.themes import material_ocean as colors

#
# mod = "mod4"
# browser = 'brave'
# terminal = "kitty"
# font = "UbuntuMono Nerd Font"
#


def load_defaults():
    defpath = join(qtile_path, 'settings', 'default_globals.json')
    with open(defpath, 'r') as f:
        defaults = json.load(f)
    return defaults


def load_theme(theme):
    themes_path = join(qtile_path, 'settings', 'themes')

    selected = join(themes_path, theme)
    with open(selected, 'r') as f:
        colors = json.load(f)
    return colors


def find_theme(l: list):
    for i in l:
        if i.startswith('---'):
            return i
    return -1


defaults = load_defaults()
mod = defaults["mod"]
browser = defaults["browser"]
terminal = defaults["terminal"]
font = defaults["font"]

# st = find_theme(sys.argv)
colors = load_theme(defaults["colors"])
# if st == -1:
#     colors = load_theme(defaults["colors"])
# else:
#     colors = load_theme(st)
