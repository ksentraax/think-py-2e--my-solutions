"""This script checks if letters appear
in a word in alphabetical order."""


def is_abecedarian(word):
    """Checks if a word contains all characters in alphabetical order.

    :param word: string
    :return: boolean value
    """
    i = 0
    while i < len(word) - 1:
        if word[i] > word[i + 1]:
            return False
        i += 1
    return True


if __name__ == "__main__":
    print(is_abecedarian('aabcd'))
