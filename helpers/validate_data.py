from jsonschema import validate, exceptions
from helpers.get_data import get_json


def record_exists(key):
    for item in get_json():
        if item['key'] == key:
            return item['value']
    return False


def json_validate(body):
    schema = {
        "type": "object",
        "required": [
            "key",
            "value"
        ],
        "properties": {
            "key": {
                "type": "string"
            },
            "value": {
                "type": "string"
            }
        },
        "additionalProperties": False
    }
    try:
        validate(body, schema)
        return True
    except (exceptions.ValidationError, exceptions.SchemaError):
        return False

