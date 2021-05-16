"""This script reads file and prints only the words with
more than 20 characters (not counting whitespace)."""


def count_characters():
    """Prints words from a file longer than 20 characters."""
    with open('words.txt', 'r') as f:
        for line in f:
            word = line.strip()
            if len(word) > 19:
                print(word)


if __name__ == '__main__':
    count_characters()
