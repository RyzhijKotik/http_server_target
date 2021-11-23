import json


def get_json_schema(schema_file):
    with open(f"tests/json_schemas/{schema_file}") as f:
        return json.load(f)
