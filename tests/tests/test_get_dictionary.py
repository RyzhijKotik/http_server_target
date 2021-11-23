import requests
from tests.test_data.request_data import host, path_dictionary_key, valid_dict
from jsonschema import validate
from tests.test_checks.constants import ResponseStatus, ResponseBody


def test_get_dictionary(get_json_schema):
    response = requests.get(host + path_dictionary_key.format(key=valid_dict['key']))

    assert response.status_code == ResponseStatus.OK
    response_body = response.json()
    assert response_body["result"] == valid_dict['value']
    validate(response_body, get_json_schema)


def test_with_invalid_key(delete_item):
    response = requests.get(host + path_dictionary_key.format(key=delete_item))

    assert response.status_code == ResponseStatus.NOT_FOUND
    assert response.text == ResponseBody.VALUE_NOT_FOUND


def test_with_empty_key():
    response = requests.get(host + path_dictionary_key.format(key=""))

    assert response.status_code == ResponseStatus.NOT_FOUND
