"""This script checks if the word contains only available letters."""


def uses_only(word, available):
    """Checks if a word contains only available characters.

    :param word: string
    :param available: available characters
    :return: boolean value
    """
    for letter in word:
        if letter not in available:
            return False
    return True


def check_only():
    """Prints words containing only available characters."""
    with open('words.txt', 'r') as f:
        for line in f:
            word = line.strip()
            if uses_only(word, 'acefhlo'):
                print(word)


if __name__ == "__main__":
    check_only()
