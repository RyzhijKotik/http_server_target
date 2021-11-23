from flask import Flask, request, make_response
from helpers.modify_data import append_data, update_data, delete_data
from helpers.validate_data import json_validate, record_exists
from helpers.date_time import current_date

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/dictionary", methods=['POST'])
def dictionary():
    if request.method == 'POST':
        body = request.json
        if not json_validate(body):
            return make_response(f"body format is invalid", 400)
        elif record_exists(body['key']):
            return make_response(f"Record with key '{body['key']}' already exists", 409)
        else:
            append_data(body)
            return make_response({"result": body['value'], "time": current_date()})


@app.route("/dictionary/<key>", methods=['GET', 'PUT', 'DELETE'])
def dictionary_key(key):
    if request.method == 'GET':
        return_value = record_exists(key)
        if return_value:
            return make_response({"result": return_value, "time": current_date()}, 200)
        else:
            return make_response("Value not found :(", 404)

    elif request.method == 'PUT':
        body = request.json
        if not json_validate(body):
            return make_response(f"body format is invalid", 400)
        elif record_exists(body['key']):
            update_data(body['key'], body['value'])
            return make_response({"result": body['value'], "time": current_date()})
        else:
            return make_response(f"Record with key '{body['key']}' not found", 404)

    elif request.method == 'DELETE':
        return_value = record_exists(key)
        if return_value:
            delete_data(key)
            return make_response({"result": None, "time": current_date()}, 200)
        else:
            return make_response({"result": None, "time": current_date()}, 200)


if __name__ == "__main__":
    app.run(debug=False)
