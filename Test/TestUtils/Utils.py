import sys
import json

ROOT_DIR = str(sys.path[1])
PARAMS_JSON_FILE = "/Test/Scripts/params.json"
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


def format_xpath(draft_xpath, format_value):
    """Creates a formatted xpath from a draft xpath and a reference value"""
    xpath = str(draft_xpath).format(VALUE=format_value)
    return xpath













