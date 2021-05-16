"""This script checks if the list is sorted in ascending order."""


def is_sorted(li):
    """Checks whether a list is sorted.

    :param li: list
    :return: boolean value
    """
    return li == sorted(li)


if __name__ == '__main__':
    print(is_sorted([1, 2, 3]))
