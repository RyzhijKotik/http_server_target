from helpers.get_data import get_json, put_json


def append_data(item):
    data = list(get_json())
    data.append(item)
    put_json(data)


def update_data(key, new_value):
    data = get_json()
    for item in data:
        if item['key'] == key:
            item['value'] = new_value
    put_json(data)


def delete_data(key):
    data = get_json()
    for item in data:
        if item['key'] == key:
            data.remove(item)
    put_json(data)
