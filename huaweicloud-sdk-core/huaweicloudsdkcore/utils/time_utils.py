import time
import datetime


def get_timestamp_utc():
    return time.mktime(datetime.datetime.utcnow().timetuple())


def get_timestamp_from_str(s, fmt):
    return time.mktime(time.strptime(s, fmt))

