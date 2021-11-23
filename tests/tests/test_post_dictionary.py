import requests
import pytest
from tests.test_data.request_data import URL, RequestData, InvalidRequestData
from helpers.json_schema import get_json_schema
from jsonschema import validate
from tests.test_checks.constants import ResponseStatus, ResponseBody


def test_post_dictionary(key_not_existing):
    body = RequestData.generate_item(key_not_existing)
    response = requests.post(URL.host + URL.path_dictionary,
                             json=body)

    assert response.status_code == ResponseStatus.OK
    response_body = response.json()
    validate(response_body, get_json_schema("default_schema.json"))
    assert response_body["result"] == body['value']


def test_post_existing_item():
    response = requests.post(URL.host + URL.path_dictionary,
                             json=RequestData.valid_dict)

    assert response.status_code == ResponseStatus.CONFLICT
    assert response.text == ResponseBody.RECORD_EXISTS.format(key=RequestData.valid_dict['key'])


@pytest.mark.parametrize("invalid_body", InvalidRequestData.invalid_dicts)
def test_post_invalid_body(invalid_body):
    response = requests.post(URL.host + URL.path_dictionary,
                             json=invalid_body)

    assert response.status_code == ResponseStatus.BAD_REQUEST
    assert response.text == ResponseBody.BODY_FORMAT_INVALID
