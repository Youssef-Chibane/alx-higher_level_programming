#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# get the absolute value of a number
if number >= 0:
    check_n = number
else:
    check_n = number * -1

# get the last digit of a number
last_d = check_n % 10

# check the given conditions
if last_d > 5:
    print(f"Last digit of {number} is {last_d} and is greater than 5")
elif last_d == 0:
    print(f"Last digit of {number} is {last_d} and is 0")
else:
    print(f"Last digit of {number} is {last_d} and is less than 6 and not 0")
