"""This script uses and passes function parameters."""


def b(z):
    """Takes an argument of c() and passes it to a().

    :param z: argument sum of c()
    """
    prod = a(z, z)
    print(z, prod)
    return prod


def a(xx, yy):
    """Takes 2 arguments of c(), performs math operations
    and passes to b().

    :param xx: argument sum of c()
    :param yy: argument sum of c()
    """
    xx = xx + 1
    return xx * yy


def c(xxx, yyy, zzz):
    """Takes 3 arguments and passes them sum to b().
    Squares the output value b().

    :param xxx: numeric variable
    :param yyy: numeric variable
    :param zzz: numeric variable
    """
    total = xxx + yyy + zzz
    square = b(total) ** 2
    return square


"""
__main__:
    x --> 1
    y --> 2

c():
    x --> 1
    y --> 5
    z --> 3
    total --> 9

b():
    z --> 9

a():
    x --> 10
    y --> 9

b():
    prod --> 90

c():
    square --> 8100
"""


if __name__ == '__main__':
    x = 1
    y = x + 1
    print(c(x, y + 3, x + y))
