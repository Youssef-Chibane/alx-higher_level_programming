#!/usr/bin/python3
"""
classcheck.py - A Python script defining a function 'inherits_from'
to check if an object inherits from a specified class.

"""


def inherits_from(obj, a_class):
    """
    Checks if the given object inherits from the specified class.

    """
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    return False
