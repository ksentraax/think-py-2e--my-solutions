"""This script uses Newton's method to find the
square root and output a table with math values."""

import math


def mysqrt(a):
    """Calculates square root using Newton's method.

    :param a: numeric value
    :return: root from a
    """
    x = a / 2
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return x


def format_number(num):
    """Takes a parameter and returns the desired 
    number of numbers after the decimal point.

    :param num: numeric value
    """
    if num % 1 == 0:
        return f'{num:<3.1f}'
    else:
        return f'{num:.11f}'


def test_square_root():
    """Prints a table showing the results of calculating
    the square root of a by various methods."""
    print('a   mysqrt(a)     math.sqrt(a)  diff')
    print('-   ---------     ------------  ----')
    a = 1.0
    while a < 10.0:
        column1 = a
        column2 = mysqrt(a)
        column3 = math.sqrt(a)
        column4 = abs(mysqrt(a) - math.sqrt(a))
        print(f'{format_number(column1)} {format_number(column2):<13} '
              f'{format_number(column3):<13} {column4:<13}')
        a = a + 1


if __name__ == '__main__':
    test_square_root()
