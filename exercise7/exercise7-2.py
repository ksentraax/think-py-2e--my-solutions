"""This script iteratively prompts the user, takes the resulting
input and evaluates it using eval, and prints the result."""


def eval_loop():
    """Takes input from the user and evaluates it
    using eval, and prints the result; it should
    continue until the user enters 'done'."""
    result = None
    while True:
        user_input = input('Write a math equation: ')
        if user_input.lower() == 'done':
            break
        result = eval(user_input)
        print(result)

    print(result)


if __name__ == '__main__':
    eval_loop()
