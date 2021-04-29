"""This script checks the length of a string and adds
leading spaces until the string is 70 characters long."""


def right_justify(s):
    """Right-justifies the string and
    fills up to 70 characters with spaces.

    :param s: string value
    :return: string
    """
    if len(s) >= 70:
        return s
    while len(s) < 70:
        s = ' ' + s
    return s


if __name__ == '__main__':
    print(right_justify('monty'))
