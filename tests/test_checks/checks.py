from datetime import datetime

def check_date_format(date):
    datetime.strptime(date, "%Y-%m-%d %H:%M")