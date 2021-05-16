"""This script takes a list, modifies it by removing
the first and last elements, and returns None."""


def chop(li):
    """Modifies list by removing the first and last elements.

    :param li: list
    :return: None
    """
    del li[1]
    del li[-1]


if __name__ == '__main__':
    t = [1, 2, 3, 4]
    print(chop(t))
