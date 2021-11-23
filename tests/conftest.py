import json
import pytest
from tests.test_data.request_data import host, path_dictionary, path_dictionary_key, valid_dict, generate_item
import requests


@pytest.fixture()
def get_json_schema():
    with open("tests/test_checks/response_schema.json") as f:
        return json.load(f)


@pytest.fixture()
def delete_item():
    key_to_delete = valid_dict['key']
    requests.delete(host + path_dictionary_key.format(key=key_to_delete))
    yield key_to_delete
    requests.post(host + path_dictionary, json=generate_item(key_to_delete))
