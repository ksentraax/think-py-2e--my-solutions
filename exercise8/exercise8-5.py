"""This script implements the Caesar cipher is a form of encryption
that involves rotating each letter by a fixed number of places."""


def rotate_word(word, rotation):
    """This function realize Caesar cypher, that offset input word.

    :param word: string value
    :param rotation: int value
    :return: encrypted string
    """
    new_word = ''
    for i in word:
        new_word += chr(ord(i) + rotation)
    return new_word


if __name__ == '__main__':
    print(rotate_word('cheer', 7))
