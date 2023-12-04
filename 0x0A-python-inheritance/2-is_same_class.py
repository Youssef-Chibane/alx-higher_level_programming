#!/usr/bin/python3
"""
classcheck.py - A Python script defining a function 'is_same_class'
to check if an object is exactly an instance of a specified class.

"""


def is_same_class(obj, a_class):
    """
    Checks if the given object is exactly an instance of the specified class.

    """
    return type(obj) is a_class
