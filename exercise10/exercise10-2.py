"""This script calculates the cumulative sum."""


def cumsum(li):
    """Creates new list where the ith element is the sum
    of the first i + 1 elements from the original list.

    :param li: list of numbers
    :return: new list with cumulative sum of elements
    """
    total = 0
    result = []
    for elem in li:
        total += elem
        result.append(total)
    return result


if __name__ == '__main__':
    t = [1, 2, 3]
    print(cumsum(t))
