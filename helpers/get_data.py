import json


def get_json(path="../data/data_json.json"):
    with open(path) as f:
        return json.load(f)


def put_json(new_json, path="../data/data_json.json"):
    with open(path, "w") as f:
        return json.dump(new_json, f)
