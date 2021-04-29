"""This script checks if the string is a palindrome."""


def is_palindrome(word):
    """Returns True if argument is a palindrome.

    :param word: string value
    :return: boolean value
    """
    return word == word[::-1]


if __name__ == '__main__':
    print(is_palindrome('noon'))
