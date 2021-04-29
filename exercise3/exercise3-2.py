"""This script outputs the value the specified number of times."""


def do_twice(f, arg):
    """Calls a function twice.

    :param f: function object
    :param arg: argument passed to the function
    """
    f(arg)
    f(arg)


def print_twice(arg):
    """Prints the argument twice.

    :param arg: anything printable
    """
    print(arg)
    print(arg)


def do_four(f, arg):
    """Calls a function four times.

    :param f: function object
    :param arg: argument passed to the function
    """
    do_twice(f, arg)
    do_twice(f, arg)


if __name__ == '__main__':
    do_twice(print_twice, 'spam')
    do_four(print_twice, 'SPAM')
