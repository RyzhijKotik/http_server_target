from helpers.get_data import get_json

host = "http://127.0.0.1:5000"

path_dictionary = "/dictionary"
path_dictionary_key = f"/dictionary/{{key}}"


path_to_data = "data\data_json.json"

valid_dict = get_json(path=path_to_data)[0]
