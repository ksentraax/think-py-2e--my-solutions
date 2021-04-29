"""This script draws 2 by 2 and 4 by 4 grids."""


# Grid with two rows & two columns.
def do_twice(f):
    """Calls a function twice.

    :param f: function object
    """
    f()
    f()


def do_four(f):
    """Calls a function four times.

    :param f: function object
    """
    do_twice(f)
    do_twice(f)


def width():
    """Prints a line with content."""
    print('+ - - - -', end=' ')


def length():
    """Prints a line with content."""
    print('|        ', end=' ')


def whole_width():
    """Print a horizontal grid line."""
    do_twice(width)
    print('+')


def whole_length():
    """Print a vertical grid line."""
    do_twice(length)
    print('|')


def row_by_two():
    """Building a grid row."""
    whole_width()
    do_four(whole_length)


def grid_by_two():
    """Building a grid."""
    do_twice(row_by_two)
    whole_width()


# Grid with four rows & four columns.
def constructor(f, a, e):
    """Function for sequential construction.

    :param f: function object
    :param a: function object
    :param e: function object
    """
    f()
    do_four(a)
    e()


def print_plus():
    """Prints a line with content."""
    print('+', end=' ')


def print_dash():
    """Prints a line with content."""
    print('-', end=' ')


def print_bar():
    """Prints a line with content."""
    print('|', end=' ')


def print_space():
    """Prints a line with content."""
    print(' ', end=' ')


def print_end():
    """Prints an empty line."""
    print()


def nothing():
    """No action is required."""
    pass


def one_width():
    """Building horizontal line."""
    constructor(nothing, print_dash, print_plus)


def one_length():
    """Building vertical line."""
    constructor(nothing, print_space, print_bar)


def four_width():
    """Building horizontal lines."""
    constructor(print_plus, one_width, print_end)


def four_length():
    """Building vertical lines."""
    constructor(print_bar, one_length, print_end)


def row_by_four():
    """Building a grid row."""
    constructor(nothing, four_length, four_width)


def grid_by_four():
    """Building a grid."""
    constructor(four_width, row_by_four, nothing)


if __name__ == "__main__":
    grid_by_two()
    grid_by_four()
