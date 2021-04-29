"""This script reads the number of seconds that have
passed since January 1, 1970 and converts them to the
current time and the number of days since the epoch."""

import time
now = time.time()


def time_since_epoch():
    """Converts seconds from epoch to current time.

    :return: current time
    """
    hours = int(now % 86400 / 3600)
    minutes = int(now % 3600 / 60)
    seconds = int(now % 60)
    return f'Current time is {hours}:{minutes}:{seconds}.'


def days_since_epoch():
    """Converts seconds from epoch to days.

    :return: days from epoch
    """
    days = int(now / 86400)
    return f'Days from Epoch: {days}.'


if __name__ == '__main__':
    print(time_since_epoch())
    print(days_since_epoch())
