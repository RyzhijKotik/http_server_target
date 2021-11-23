from helpers.get_data import get_json

host = "http://127.0.0.1:5000"

path_dictionary = "/dictionary"
path_dictionary_key = f"/dictionary/{{key}}"


path_to_data = "data\data_json.json"

valid_dict = get_json(path=path_to_data)[0]

invalid_dicts = [None,
                 {},
                 {"value": "no_key"},
                 {"key": "no_value"},
                 {"key": "100500"}, {"value": "too_many_fields"}, {"another_field": "error"}]


def generate_item(key):
    return {"key": key, "value": f"value for key {key}"}

