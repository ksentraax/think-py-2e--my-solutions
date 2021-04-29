"""This script checks if Fermat’s theorem is
confirmed and prompts the user to input values."""


def check_fermat(a, b, c, n):
    """Checks if Fermat's theorem is true.

    :param a: positive integer value
    :param b: positive integer value
    :param c: positive integer value
    :param n: positive integer value
    :return: result string
    """
    if n > 2 and (a**n + b**n == c**n):
        return 'Holy smokes, Fermat was wrong!'
    else:
        return 'No, that does not work.'


def check_numbers():
    """Prompts the user to enter values for Fermat's theorem."""
    a = int(input('Choose a number for a:'))
    b = int(input('Choose a number for b:'))
    c = int(input('Choose a number for c:'))
    n = int(input('Choose a number for n:'))
    return check_fermat(a, b, c, n)


if __name__ == '__main__':
    print(check_numbers())
