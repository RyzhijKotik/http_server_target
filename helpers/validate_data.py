from jsonschema import validate, exceptions
from helpers.get_data import get_json

path_to_data = "../data/"


def record_exists(key):
    for item in get_json():
        if item['key'] == key:
            return item['value']
    return False


def json_validate(body):
    try:
        validate(body, get_json(path=f"{path_to_data}data_schema.json"))
        return True
    except (exceptions.ValidationError, exceptions.SchemaError):
        return False

