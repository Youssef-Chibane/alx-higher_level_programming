#!/usr/bin/python3
"""
Write a Python object to a text file using its JSON representation.

"""
import json


def save_to_json_file(my_obj, filename):
    """
    Parameters:
    - my_obj: The Python object to be written to the file.
    - filename (str): The name of the file to write the JSON representation to.

    """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
