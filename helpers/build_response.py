from flask import make_response
from datetime import datetime


def current_date():
    return datetime.isoformat(datetime.now(), sep=' ', timespec='minutes')


def default_response(value):
        return make_response({"result": value, "time": current_date()})


def error_response(message, code):
    return make_response(message, code)

