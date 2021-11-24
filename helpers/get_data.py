import json

data_json_path = "data/data_json.json"


def get_json(path=data_json_path):
    with open(path) as f:
        return json.load(f)


def put_json(new_json, path=data_json_path):
    with open(path, "w") as f:
        return json.dump(new_json, f)
