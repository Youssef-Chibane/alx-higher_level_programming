#!/usr/bin/python3
"""
Write the specified text to a file with the given filename.

"""


def write_file(filename="", text=""):
    """
    Parameters:
    - filename (str): The name of the file to write to. If the file already exists,
    its content will be overwritten. If the file does not exist,
    a new file with the specified filename will be created.
    - text (str): The text to be written to the file.

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
