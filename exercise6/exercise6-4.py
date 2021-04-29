"""This script checks if a is a power of b."""


def is_power(a, b):
    """Checks if a is a power of b.

    :param a: numeric value
    :param b: numeric value
    :return: boolean value
    """
    if a == 1:
        return True
    elif a % b == 0 and is_power(a/b, b):
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_power(9, 3))
