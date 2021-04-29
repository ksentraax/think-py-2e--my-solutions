"""This script uses Srinivasa Ramanujan's formula
to compute and return an estimate of π."""

from math import sqrt


def factorial(number):
    """Calculates the factorial of a number.

    :param number: int value
    :return: factorial of a number
    """
    if number == 0:
        return 1
    else:
        factorial_num = number * factorial(number - 1)
    return factorial_num


def estimate_pi():
    """Uses Srinivasa Ramanujan's formula to
    obtain a numerical approximation of 1 / π.

    :return: pi value
    """
    total = 0
    k = 0
    while True:
        num = factorial(4*k) * (1103 + 26390*k)
        den = factorial(k)**4 * 396**(4 * k)
        term = (2 * sqrt(2) / 9801) * num / den
        total += term

        if abs(term) < 1e-15:
            break
        k += 1
    return 1 / total


if __name__ == '__main__':
    print(estimate_pi())
