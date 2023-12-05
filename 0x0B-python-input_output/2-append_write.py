#!/usr/bin/python3
"""
Append the specified text to the end of a file with the given filename.

"""


def append_write(filename="", text=""):
    """
    Parameters:
    - filename (str): The name of the file to which text will be appended.
    If the file does not exist, a new file with the specified
    filename will be created.
    - text (str): The text to be appended to the file.

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
