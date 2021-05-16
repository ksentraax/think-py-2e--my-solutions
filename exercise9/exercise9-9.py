"""This script calculates cases when the age of the mother
and daughter, given the difference in age, was a palindrome
and returns the current age of the daughter by the condition."""


ages = [str(i).zfill(2) for i in range(1, 100)]


def age():
    """Calculates the possible age of the daughter."""
    diff = 15
    while diff <= 45:
        ages_list = []
        for i in range(0, 99):
            if (i + diff) >= 99:
                pass
            elif ages[i][::-1] == ages[i + diff]:
                ages_list.append([ages[i], ages[i + diff]])
        if len(ages_list) == 8:
            return ages_list
        else:
            diff += 1


if __name__ == '__main__':
    print('Palindrome cases:')
    for i in age():
        print(i[0])
    print(f"Daughter's current age: {age()[5][0]}")
