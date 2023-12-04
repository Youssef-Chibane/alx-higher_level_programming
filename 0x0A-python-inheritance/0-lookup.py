#!/usr/bin/python3
"""
lookup.py - A Python script to get a list of
attributes and methods of an object.

"""


def lookup(obj):
    """
    Returns a list of attributes and methods of the given object.

    """
    return dir(obj)
