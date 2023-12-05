#!/usr/bin/python3
"""
function that returns an object (Python data structure)
represented by a JSON string.

"""
import json


def from_json_string(my_str):
    """
    Parameters:
    - json_string (str): The JSON-formatted string to be
    converted to a Python object.

    """

    python_object = json.loads(my_str)
    return python_object
