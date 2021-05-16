"""This script checks if two words are anagrams."""


def is_anagram(word1, word2):
    """Checks whether two words are anagrams.

    :param word1: string
    :param word2: string
    :return: boolean value
    """
    return sorted(word1) == sorted(word2)


if __name__ == '__main__':
    print(is_anagram('thing', 'night'))
