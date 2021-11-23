import pytest
from tests.test_data.request_data import host, path_dictionary, path_dictionary_key, valid_dict, generate_item
import requests


@pytest.fixture()
def key_to_delete():
    key = valid_dict['key']
    yield key
    requests.post(host + path_dictionary, json=generate_item(key))


@pytest.fixture()
def key_not_existing():
    key = valid_dict['key']
    requests.delete(host + path_dictionary_key.format(key=key))
    yield key
    requests.post(host + path_dictionary, json=generate_item(key))


