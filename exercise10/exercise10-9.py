"""This script uses functions to open a file,
they write each word as an element of a new list
in two ways and display their elapsed time."""

import time


def version1():
    """Opens a file and writes each word as a list item.
    Version 1 using the append() method.

    :return: list
    """
    file = open("words.txt")
    li = []
    for element in file:
        word = element.strip()
        li.append(word)
    return li


def version2():
    """Opens a file and writes each word as a list item.
    Version 2 using the idiom t = t + [x].

    :return: list
    """
    file = open("words.txt")
    t = []
    for element in file:
        x = element.strip()
        t = t + [x]
    return t


def main():
    """Counts the time spent on performing functions.

    :return: elapsed time
    """
    start = time.time()
    version1()
    end = time.time() - start
    print(f'The version1() function does the job in {end} seconds.')

    start2 = time.time()
    version2()
    end2 = time.time() - start2
    print(f'The version2() function does the job in {end2} seconds.')


if __name__ == "__main__":
    main()
