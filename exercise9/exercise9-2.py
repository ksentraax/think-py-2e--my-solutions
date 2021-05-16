"""This script checks a word for the letter e and
calculates the percentage of such words in the list."""


def has_no_e(word):
    """Checks a word for the letter e.

    :param word: string
    :return: boolean value
    """
    return 'e' not in word


def percentage():
    """Prints only the words that have no e
    and calculate the percentage of words."""
    num_of_words = 0
    count = 0
    with open('words.txt', 'r') as f:
        for line in f:
            num_of_words += 1
            word = line.strip()
            if has_no_e(word):
                print(word)
                count += 1
    percent = (count / num_of_words) * 100
    print(f'Percent: {percent}%.')


if __name__ == '__main__':
    percentage()
