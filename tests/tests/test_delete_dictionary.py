import pytest
import requests
from jsonschema import validate

from helpers.constants import ResponseStatus, path_to_json_schemas
from helpers.get_data import get_json
from tests.test_data.request_data import URL, InvalidRequestData
from tests.test_checks.checks import check_date_format


def test_delete_dictionary(key_to_delete):
    response = requests.delete(URL.host + URL.path_dictionary_key.format(key=key_to_delete))

    assert response.status_code == ResponseStatus.OK
    response_body = response.json()
    validate(response_body, get_json(path=f"{path_to_json_schemas}empty_result.json"))
    assert response_body["result"] is None
    check_date_format(response_body["time"])


@pytest.mark.parametrize("invalid_key", InvalidRequestData.invalid_keys)
def test_delete_invalid_keys(invalid_key):
    response = requests.delete(URL.host + URL.path_dictionary_key.format(key=invalid_key))

    assert response.status_code == ResponseStatus.OK
    response_body = response.json()
    validate(response_body, get_json(path=f"{path_to_json_schemas}empty_result.json"))
    assert response_body["result"] is None
    check_date_format(response_body["time"])

