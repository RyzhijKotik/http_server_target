import requests
from jsonschema import validate

from helpers.constants import ResponseStatus, ResponseBody, path_to_json_schemas
from helpers.get_data import get_json
from tests.test_data.request_data import URL, RequestData


def test_get_dictionary():
    request_dict = RequestData.valid_dict
    response = requests.get(URL.host + URL.path_dictionary_key
                                          .format(key=request_dict['key']))

    assert response.status_code == ResponseStatus.OK
    response_body = response.json()
    validate(response_body, get_json(path=f"{path_to_json_schemas}default_schema.json"))
    assert response_body["result"] == request_dict['value']


def test_with_invalid_key(key_not_existing):
    response = requests.get(URL.host + URL.path_dictionary_key.format(key=key_not_existing))

    assert response.status_code == ResponseStatus.NOT_FOUND
    assert response.text == ResponseBody.VALUE_NOT_FOUND


def test_with_empty_key():
    response = requests.get(URL.host + URL.path_dictionary_key.format(key=""))

    assert response.status_code == ResponseStatus.NOT_FOUND
