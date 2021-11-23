from data.data import data_json


def append_data(item):
    data_json.append(item)


def update_data(key, new_value):
    for item in data_json:
        if item['key'] == key:
            item['value'] = new_value


def delete_data(key):
    for item in data_json:
        if item['key'] == key:
            data_json.remove(item)
