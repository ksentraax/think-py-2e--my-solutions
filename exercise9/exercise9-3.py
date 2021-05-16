"""This script checks if a word contains
forbidden letters and counts those words."""


def avoids(word, forbidden):
    """Checks if a word contains a string of forbidden letters.

    :param word: string
    :param forbidden: string of forbidden letters
    :return: boolean value
    """
    for letter in word:
        if letter in forbidden:
            return False
    return True


def avoids_forbidden():
    """Prompts the user to enter a string of forbidden letters
    and prints the number of words that do not contain any of them."""
    user_input = input("Enter a string of forbidden letters:")
    count = 0
    with open('words.txt', 'r') as f:
        for line in f:
            word = line.strip()
            if avoids(word, user_input):
                count += 1
        print(count)


if __name__ == '__main__':
    avoids_forbidden()
