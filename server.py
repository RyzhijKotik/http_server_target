from flask import Flask, request, make_response
from helpers.modify_data import append_data, update_data, delete_data
from helpers.validate_data import json_validate, record_exists
from helpers.build_response import default_response, error_response
from helpers.constants import ResponseBody, ResponseStatus

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/dictionary", methods=['POST'])
def dictionary():
    if request.method == 'POST':
        body = request.json
        if not json_validate(body):
            return error_response(ResponseBody.BODY_FORMAT_INVALID, ResponseStatus.BAD_REQUEST)
        elif record_exists(body['key']) != False:
            return make_response(f"Record with key '{body['key']}' already exists", 409)
        else:
            append_data(body)
            return default_response(body['value'])

#TODO убрать копипасту в респонсах

@app.route("/dictionary/<key>", methods=['GET', 'PUT', 'DELETE'])
def dictionary_key(key):
    if request.method == 'GET':
        return_value = record_exists(key)
        if return_value != False:
            return default_response(return_value)
        else:
            return error_response(ResponseBody.VALUE_NOT_FOUND, ResponseStatus.NOT_FOUND)

    elif request.method == 'PUT':
        body = request.json
        if not json_validate(body):
            return make_response("body format is invalid", 400)
        elif record_exists(body['key']) != False:
            update_data(body['key'], body['value'])
            return default_response(body['value'])
        else:
            return make_response(f"Record with key '{body['key']}' not found", 404)

    elif request.method == 'DELETE':
        return_value = record_exists(key)
        if return_value != False:
            delete_data(key)
        return default_response(None)


if __name__ == "__main__":
    app.run(debug=False)
