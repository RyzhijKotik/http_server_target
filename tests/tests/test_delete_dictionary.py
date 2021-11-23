import requests
from jsonschema import validate
from helpers.json_schema import get_json_schema
from tests.test_data.request_data import host, path_dictionary_key, valid_dict
from tests.test_checks.constants import ResponseStatus


def test_delete_dictionary(key_to_delete):
    response = requests.delete(host + path_dictionary_key.format(key=key_to_delete))

    assert response.status_code == ResponseStatus.OK
    response_body = response.json()
    validate(response_body, get_json_schema("empty_result.json"))
    assert response_body["result"] is None
