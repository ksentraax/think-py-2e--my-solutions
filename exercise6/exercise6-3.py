"""This script checks if the string is a palindrome."""


def first(word):
    """Returns the first character from the string.

    :param word: input string value
    :return: first string element
    """
    return word[0]


def last(word):
    """Returns the last character from the string.

    :param word: input string value
    :return: last string element
    """
    return word[-1]


def middle(word):
    """Returns all character from the string except the first and last.

    :param word: input string value
    :return: middle element of string
    """
    return word[1:-1]


def is_palindrome(word):
    """Return True if argument is a palindrome.

    :param word: input string value
    :return: boolean value
    """
    if len(word) <= 1:
        return True
    elif first(word) == last(word):
        if len(middle(word)) <= 1:
            return True
        elif len(middle(word)) > 1:
            return is_palindrome(middle(word))
    else:
        return False


if __name__ == '__main__':
    print(is_palindrome('noon'))
