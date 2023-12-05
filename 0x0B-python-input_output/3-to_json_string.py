#!/usr/bin/python3
"""
function that returns the JSON representation of an object (string).

"""
import json


def to_json_string(my_obj):
    """
    Parameters:
    - my_obj: The Python object to be converted to JSON.

    """

    json_representation = json.dumps(my_obj)
    return json_representation
