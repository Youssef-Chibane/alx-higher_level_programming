#!/usr/bin/python3
"""
Write a Python object to a text file using its JSON representation.

"""
import json


def load_from_json_file(filename):
    """
    Parameters:
    - my_obj: The Python object to be written to the file.
    - filename (str): The name of the file to write the JSON representation to.

    """

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
