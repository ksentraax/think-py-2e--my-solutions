"""This script performs a recursive algorithm,
taking 2 integer variables as input."""


def recurse(n, s):
    """Calls itself until the decrement reaches zero;
    for each step of decrement, the variable is increased

    :param n: positive integer value
    :param s: integer value
    """
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)


"""
__main__:
    None
recurse:
    n --> 3
    s --> 0
recurse:
    n --> 2
    s --> 3
recurse:
    n --> 1
    s --> 5
recurse:
    n --> 0
    s --> 6
"""


if __name__ == '__main__':
    recurse(3, 0)
