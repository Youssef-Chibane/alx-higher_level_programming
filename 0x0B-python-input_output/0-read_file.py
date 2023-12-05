#!/usr/bin/python3
"""
read_file function reads and prints the contents of a file.

"""


def read_file(filename=""):
    """
    Parameters: filename (str): The name of the file to be read.
    Default is an empty string,
    in which case the function reads a file named 'my_file_0.txt'.
    """

    with open(filename, 'r') as f:
        for line in f:
            print(line, end='')
    print()
