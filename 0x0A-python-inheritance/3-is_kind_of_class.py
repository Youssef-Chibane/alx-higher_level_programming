#!/usr/bin/python3
"""
classcheck.py - A Python script defining a function 'is_kind_of_class' to check
if an object is an instance or a subclass instance of a specified class.

"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the given object is an instance or
    a subclass instance of the specified class.

    """
    return isinstance(obj, a_class)
