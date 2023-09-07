#!/usr/bin/python3
from sys import argv

args_number = len(argv)

# print number of arguments.
if args_number - 1 == 0:
    print("{:d} arguments.".format(args_number - 1))
elif args_number - 1 == 1:
    print("{:d} argument:".format(args_number - 1))
else:
    print("{:d} arguments:".format(args_number - 1))

# print the argument with their indexes
for index, argument in enumerate(argv):
    if index != 0:
        print("{:d}: {:s}".format(index, argument))
