from copy import deepcopy

import pytest
import requests
from jsonschema import validate

from helpers.constants import ResponseStatus, ResponseBody, path_to_json_schemas
from helpers.get_data import get_json
from tests.test_data.request_data import URL, RequestData, InvalidRequestData


def test_put_dictionary():
    new_dict = deepcopy(RequestData.valid_dict)
    new_dict["value"] = f"new {RequestData.valid_dict['value']}"
    response = requests.put(URL.host + URL.path_dictionary_key.format(key=new_dict["key"]),
                            json=new_dict)

    assert response.status_code == ResponseStatus.OK
    response_body = response.json()
    validate(response_body, get_json(path=f"{path_to_json_schemas}default_schema.json"))
    assert response_body["result"] == new_dict["value"]


def test_put_not_existing_item(key_not_existing):
    body = RequestData.generate_item(key_not_existing)
    response = requests.put(URL.host + URL.path_dictionary_key.format(key=key_not_existing),
                             json=body)

    assert response.status_code == ResponseStatus.NOT_FOUND
    assert response.text == ResponseBody.RECORD_NOT_FOUND.format(key=RequestData.valid_dict['key'])


@pytest.mark.parametrize("invalid_body", InvalidRequestData.invalid_dicts)
def test_put_invalid_body(invalid_body):
    response = requests.put(URL.host + URL.path_dictionary_key.format(key="test"),
                             json=invalid_body)

    assert response.status_code == ResponseStatus.BAD_REQUEST
    assert response.text == ResponseBody.BODY_FORMAT_INVALID
