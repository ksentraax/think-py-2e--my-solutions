"""This script performs calculations using mathematical operators."""

# Calculate the volume of a sphere with a radius of 5
v = 4/3 * 3.141592653589793 * 5**3
print(f'The volume of a sphere is {v:.2f}m3.')

# Calculate the total wholesale cost of copies of books
price_book = float(input('The cover price of a book is '))
book = price_book - price_book*0.4
copies = int(input('Books copies count is '))
all_book = book * copies
other_copies = copies - 1
first_copy = copies-other_copies
price_copies = other_copies*0.75 + first_copy*3
print(f'The total wholesale cost is {all_book+price_copies:.02f}$.')

# Calculate time in hours and minutes if you leave home at 6:52 am
start = 6*3600 + 52*60
first_temp = 8*60 + 15
second_temp = 7*60 + 12
finish = start + first_temp*2 + second_temp*3
finish_hour = finish // 3600
finish_minutes = (finish // 60) % 60
print(f'You will go home for breakfast at {finish_hour}:{finish_minutes} am.')
