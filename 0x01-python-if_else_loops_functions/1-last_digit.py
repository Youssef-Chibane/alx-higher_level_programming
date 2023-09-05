#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# get the absolute value of a number
if number >= 0:
    check_n = number
else:
    check_n = number * -1

# get the last last_d of a number
last_d = check_n % 10

print(f"Last last_d of {number:d} is {last_d:d} and is ", end="")
if last_d > 5:
    print("greater than 5")
elif last_d == 0:
    print("0")
else:
    print("less than 6 and not 0")
