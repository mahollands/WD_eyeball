"""
Functions for formatting the time and date
"""
import time


def date_string():
    """
    Nicely formatting current date
    """
    t = time.localtime()
    return f"{t.tm_year:04}-{t.tm_mon:02}-{t.tm_mday:02}"


def time_string():
    """
    Nicely formatting current time
    """
    t = time.localtime()
    return f"{t.tm_hour:02}:{t.tm_min:02}"
