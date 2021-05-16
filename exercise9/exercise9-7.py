"""This script checks if a word contains three
consecutive double letters and finds those words."""


def is_double(word):
    """Checks if a word contains three consecutive double letters.

    :param word: string
    :return: boolean value
    """
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i+1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            count = 0
            i += 1
    return False


def find_double():
    """Prints words with three sequences of double letters."""
    with open('words.txt', 'r') as f:
        for line in f:
            word = line.strip()
            if is_double(word):
                print(word)


if __name__ == '__main__':
    find_double()
