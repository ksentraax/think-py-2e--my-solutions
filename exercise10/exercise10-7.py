"""This script checks the list for duplicates."""


def has_duplicates(li):
    """Checks if there is any element that appears more than once.

    :param li: list
    :return: boolean value
    """
    li.sort()
    for i in range(len(li)-1):
        if li[i] == li[i+1]:
            return True
    return False


if __name__ == '__main__':
    print(has_duplicates([1, 1, 5, 4, 2]))
