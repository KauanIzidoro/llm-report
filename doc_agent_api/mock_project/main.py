import time


def calendar():
    months = [
        "JAN",
        "FEB",
        "MAR",
        "APR",
        "MAY",
        "JUN",
        "JUL",
        "AUG",
        "SEP",
        "OCT",
        "NOV",
        "DEC",
    ]
    localdate = time.localtime()
    return {
        "Year": localdate.tm_year,
        "Month": months[localdate.tm_mon - 1],
        "Day": localdate.tm_mday,
        "Time": f"{localdate.tm_hour}:{localdate.tm_min}:{localdate.tm_sec}",
    }


def xyz():
    return "xyz"

