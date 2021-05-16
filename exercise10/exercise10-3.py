"""This script takes a list and returns a new list that
contains all but the first and last elements."""


def middle(li):
    """Takes a list and returns a new list without
    the first and last elements.

    :param li: list
    :return: new list
    """
    return li[1:-1]


if __name__ == '__main__':
    t = [1, 2, 3, 4]
    print(middle(t))
