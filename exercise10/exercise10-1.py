"""This script takes a list of lists of integers
and adds the items from all nested lists."""


def nested_sum(li):
    """Calculates the sum of the elements from all of the nested lists.

    :param li: list of lists of integers
    :return: sum of the elements
    """
    total = 0
    for elem in li:
        total += sum(elem)
    return total


if __name__ == '__main__':
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))
