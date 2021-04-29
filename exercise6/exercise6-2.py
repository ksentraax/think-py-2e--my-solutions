"""This script evaluates the Ackermann function."""


def ack(m, n):
    """Evaluates the Ackermann function.

    :param m: integers greater than 0
    :param n: integers greater than 0
    :return: natural integer value
    """
    if m == 0:
        return n + 1
    elif n == 0 and m > 0:
        return ack(m - 1, 1)
    elif n > 0 and m > 0:
        return ack(m - 1, ack(m, n - 1))


if __name__ == "__main__":
    print(ack(3, 4))
