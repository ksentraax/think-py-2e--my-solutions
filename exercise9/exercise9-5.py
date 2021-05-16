"""This script checks if the word contains all available letters."""


def uses_all(word, required):
    """Checks if a word contains all available characters.

    :param word: string
    :param required: required characters
    :return: boolean value
    """
    for letter in required:
        if letter not in word:
            return False
    return True


def count_all():
    """Counts how many words contain available characters."""
    count = 0
    with open('words.txt', 'r') as f:
        for line in f:
            word = line.strip()
            if uses_all(word, 'aeiou'):
                count += 1
        print(count)


if __name__ == '__main__':
    count_all()
