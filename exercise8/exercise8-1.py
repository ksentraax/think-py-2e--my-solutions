"""This script test 10 functions that implement various
built-in string manipulation methods using a test string."""


string_test = 'i havE read a great bOOk'
list_test = ['i', 'have', 'read', 'a', 'great', 'book']


def to_capitalize(string):
    """Returns a copy of the string with its first
    character titlecase and the rest lowercased.

    :param string: string value
    :return: string with the first character titlecase
    """
    result = string.capitalize()
    return result


def to_count(string, substring):
    """Returns the number of non-overlapping occurrences
    of substring in the string.

    :param string: string value
    :param substring: string value
    :return: integer value
    """
    result = string.count(substring)
    return result


def to_find(string, substring):
    """Returns the lowest index in the string where substring is found.

    :param string: string value
    :param substring: string value
    :return: index of the first occurrence
    """
    result = string.find(substring)
    return result


def to_replace(string, old, new):
    """Returns a copy of the string with all occurrences
    of substring old replaced by new.

    :param string: string value
    :param old: string value
    :param new: string value
    :return: string with old substring replaced by new
    """
    result = string.replace(old, new)
    return result


def to_split(string, sep=None):
    """Returns a list of the words in the string,
    using sep as the delimiter string.

    :param string: string value
    :param sep: delimiter string
    :return: list from string
    """
    result = string.split(sep)
    return result


def to_join(li, iterable):
    """Returns a string which is the concatenation
    of the strings in iterable.

    :param li: list
    :param iterable: string value
    :return: string
    """
    result = iterable.join(li)
    return result


def to_format(string):
    """Returns a copy of the string where each replacement field
     is replaced with the string value of the corresponding argument.

    :param string: string variable.
    :return: string, that executes format() method.
    """
    result = 'I have read a great {}'.format(string)
    return result


def to_rjust(string, width, fillchar):
    """Return the string right justified in a string of length width.

    :param string: string value
    :param width: integer, the required length of the string
    :param fillchar: placeholder character, space by default ASCII
    :return: string of specified length
    """
    result = string.rjust(width, fillchar)
    return result


def to_upper(string):
    """Returns a copy of the string with all the cased
    characters converted to uppercase.

    :param string: string value
    :return: string with all characters uppercase
    """
    result = string.upper()
    return result


def to_lower(string):
    """Returns a copy of the string with all the cased
    characters converted to lowercase.

    :param string: string value
    :return: string with all characters lowercase
    """
    result = string.lower()
    return result


def main():
    print(to_capitalize(string_test))
    print(to_count(string_test, 'a'))
    print(to_find(string_test, 'read'))
    print(to_replace(string_test, 'bOOk', 'magazine'))
    print(to_split(string_test))
    print(to_join(list_test, ' '))
    print(to_format('book'))
    print(to_rjust(string_test, 72, '.'))
    print(to_upper(string_test))
    print(to_lower(string_test))


if __name__ == "__main__":
    main()
