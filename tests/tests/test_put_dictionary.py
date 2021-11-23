import requests
import pytest
from tests.test_data.request_data import host, path_dictionary_key, generate_item, valid_dict, invalid_dicts
from jsonschema import validate
from tests.test_checks.constants import ResponseStatus, ResponseBody
from copy import deepcopy


def test_put_dictionary(get_json_schema):
    new_dict = deepcopy(valid_dict)
    new_dict["value"] = f"new {valid_dict['value']}"
    response = requests.put(host + path_dictionary_key, json=new_dict)

    assert response.status_code == ResponseStatus.OK
    response_body = response.json()
    assert response_body["result"] == new_dict["value"]
    validate(response_body, get_json_schema)


def test_put_not_existing_item(delete_item):
    body = generate_item(delete_item)
    response = requests.put(host + path_dictionary_key,
                             json=body)

    assert response.status_code == ResponseStatus.NOT_FOUND
    assert response.text == ResponseBody.RECORD_NOT_FOUND.format(key=valid_dict['key'])


@pytest.mark.parametrize("invalid_body", invalid_dicts)
def test_put_invalid_body(invalid_body):
    response = requests.put(host + path_dictionary_key,
                             json=invalid_body)

    assert response.status_code == ResponseStatus.BAD_REQUEST
    assert response.text == ResponseBody.BODY_FORMAT_INVALID
