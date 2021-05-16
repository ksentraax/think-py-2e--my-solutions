"""This script checks six-digit numbers for
the requirements described in the book."""


def search_num():
    """Tests all the six-digit numbers and prints
     any numbers that satisfy requirements.

    :return: int values
    """
    for i in range(100000, 1000000):
        if str(i)[2:] == str(i)[:1:-1]:
            i += 1
            if str(i)[1:] == str(i)[5:0:-1]:
                i += 1
                if str(i)[1:-1] == str(i)[-2:0:-1]:
                    i += 1
                    if str(i) == str(i)[::-1]:
                        print(i - 3)


if __name__ == '__main__':
    search_num()
