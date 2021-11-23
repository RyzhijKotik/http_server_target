class ResponseStatus:
    OK = 200
    NOT_FOUND = 404
    CONFLICT = 409
    BAD_REQUEST = 400


class ResponseBody:
    VALUE_NOT_FOUND = "Value not found :("
    RECORD_EXISTS = "Record with key '{key}' already exists"
    BODY_FORMAT_INVALID = "body format is invalid"
