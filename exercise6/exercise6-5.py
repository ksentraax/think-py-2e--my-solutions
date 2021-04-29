"""This script finds the greatest common divisor (GCD) of a and b."""


def gcd(a, b):
    """Finds the largest positive integer that divides
    all the numbers in the set without remainder.

    :param a: int value
    :param b: int value
    :return: greatest common divisor
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


if __name__ == '__main__':
    print(gcd(140, 25))
