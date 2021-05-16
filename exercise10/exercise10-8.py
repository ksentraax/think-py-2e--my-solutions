"""This script checks the number of birthday
matches in a given number of people."""

from random import randint


def has_duplicates(li):
    """Checks if there is any element that appears more than once.

    :param li: list
    :return: boolean value
    """
    li.sort()
    for i in range(len(li)-1):
        if li[i] == li[i+1]:
            return True
    return False


def random_dates(num):
    """Generates a list of integers from 1 to 366 of length num.

    :param num: integer value
    :return: list of integer
    """
    dates = []
    for i in range(num):
        dates.append(randint(1, 366))
    return dates


def count_matches(students, simulation):
    """Checks what the probability of a match is.

    :param students: integer value
    :param simulation: integer value
    :return: integer value
    """
    count = 0
    for i in range(simulation):
        dates = random_dates(students)
        if has_duplicates(dates):
            count += 1
    probability = count * 0.1
    return f'Probability of matches: {probability}%'


if __name__ == '__main__':
    print(count_matches(23, 1000))
