import requests
import pytest
from jsonschema import validate
from helpers.json_schema import get_json_schema
from tests.test_data.request_data import URL, InvalidRequestData
from tests.test_checks.constants import ResponseStatus


def test_delete_dictionary(key_to_delete):
    response = requests.delete(URL.host + URL.path_dictionary_key.format(key=key_to_delete))

    assert response.status_code == ResponseStatus.OK
    response_body = response.json()
    validate(response_body, get_json_schema("empty_result.json"))
    assert response_body["result"] is None


@pytest.mark.parametrize("invalid_key", InvalidRequestData.invalid_keys)
def test_delete_invalid_keys(invalid_key):
    response = requests.delete(URL.host + URL.path_dictionary_key.format(key=invalid_key))

    assert response.status_code == ResponseStatus.OK
    response_body = response.json()
    validate(response_body, get_json_schema("empty_result.json"))
    assert response_body["result"] is None

