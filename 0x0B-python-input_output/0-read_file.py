#!/usr/bin/python3

def read_file(filename=""):
    """
    read_file function reads and prints the contents of a file.

    """
    with open(filename, 'r') as f:
        for line in f:
            print(line, end='')
    print()
