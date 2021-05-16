"""This script finds all pairs of words that interlock."""


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


def interlock(word_list, word):
    """Checks if a word contains two interleaved words.

    :param word_list: list of words
    :param word: string
    :return: boolean value
    """
    word1 = word[::2]
    word2 = word[1::2]
    return in_bisect(word_list, word1) and in_bisect(word_list, word2)


def interlock_search(word_list, word, n=3):
    """Checks if a word contains three interleaved words.

    :param word_list: list of words
    :param word: string
    :param n: number of interleaved words
    :return: boolean value
    """
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(word_list, inter):
            return False
    return True


if __name__ == '__main__':
    word_list = get_list()

    for word in word_list:
        if interlock(word_list, word):
            print(word, word[::2], word[1::2])

    for word in word_list:
        if interlock_search(word_list, word, 3):
            print(word, word[0::3], word[1::3], word[2::3])
