import pytest
from tests.test_data.request_data import URL, RequestData
import requests


@pytest.fixture()
def key_to_delete():
    key = RequestData.valid_dict['key']
    yield key
    requests.post(URL.host + URL.path_dictionary,
                  json=RequestData.generate_item(key))


@pytest.fixture()
def key_not_existing():
    key = RequestData.valid_dict['key']
    requests.delete(URL.host + URL.path_dictionary_key.format(key=key))
    yield key
    requests.post(URL.host + URL.path_dictionary,
                  json=RequestData.generate_item(key))


