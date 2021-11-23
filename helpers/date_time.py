from datetime import datetime


def current_date():
    return datetime.isoformat(datetime.now(), sep=' ', timespec='minutes')