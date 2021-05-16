"""This script finds all the reverse pairs in the word list."""


def get_list():
    """Opens a file and writes each word as a list item.

    :return: sorted list
    """
    file = open("words.txt")
    li = []
    for element in file:
        word = element.strip()
        li.append(word)
    return li


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


def reverse_pair(word_list, word):
    """Returns reverse pairs if such exists.

    :param word_list: list of words
    :param word: string
    :return: reverse pair
    """
    return in_bisect(word_list, word[::-1])


if __name__ == '__main__':
    word_list = get_list()

    for word in word_list:
        if reverse_pair(word_list, word):
            print(word, word[::-1])
