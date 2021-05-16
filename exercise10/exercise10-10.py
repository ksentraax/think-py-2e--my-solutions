"""This script checks if the item is in the sorted list."""


def get_list():
    """Opens a file and writes each word as a list item.

    :return: sorted list
    """
    file = open("words.txt")
    li = []
    for element in file:
        word = element.strip()
        li.append(word)
    return sorted(li)


def in_bisect(li, item):
    """Checks if the given item is in the list.

    :param li: sorted list
    :param item: target value
    :return: boolean value
    """
    low = 0
    high = len(li) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = li[mid]
        if guess == item:
            return True
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return False


if __name__ == '__main__':
    print(in_bisect(get_list(), 'acres'))
