"""This script checks the possibility of
creating a triangle with given sides."""


def is_triangle(a, b, c):
    """Checks whether or cannot form a triangle with given sides.

    :param a: positive integer argument
    :param b: positive integer argument
    :param c: positive integer argument
    :return: result string
    """
    if a + b >= c and a + c >= b and b + c >= a:
        return 'Yes'
    else:
        return 'No'


def triangle_numbers():
    """Prompts the user to input values
    for the three sides of a triangle."""
    a = int(input('Choose a number for a:'))
    b = int(input('Choose a number for b:'))
    c = int(input('Choose a number for c:'))
    return is_triangle(a, b, c)


if __name__ == '__main__':
    print(triangle_numbers())
