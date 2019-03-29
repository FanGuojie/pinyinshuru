import json


def readJson(filename):
    with open(filename, 'r') as f:
        jsObj = f.read()
        data = json.loads(jsObj)
    return data


EMISSION_FILE = "./data/emission.json"
TRANSITION_FILE = "./data/transition.json"
INIT_FILE = "./data/init.json"
emission=readJson(EMISSION_FILE)
transition=readJson(TRANSITION_FILE)
init=readJson(INIT_FILE)
