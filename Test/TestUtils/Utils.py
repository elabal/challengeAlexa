import sys
import json

ROOT_DIR = str(sys.path[1])
PARAMS_JSON_FILE = "/Test/Scripts/param.json"
"""Defining the paths for the root directory and the parameters JSON file"""


def get_param(key):
    """Gets a parameter value for a designed key from params.json"""
    with open(ROOT_DIR + PARAMS_JSON_FILE) as f:
        data = json.load(f)
        return data[key]


def save_param(key, value):
    """Stores the obtained value and the designed key as a parameter in params.json"""
    with open(ROOT_DIR + PARAMS_JSON_FILE) as f:
        data = json.load(f)
    data[key] = value
    with open(ROOT_DIR + PARAMS_JSON_FILE, 'w') as f:
        f.write(json.dumps(data, indent=4, separators=(',', ': ')))













