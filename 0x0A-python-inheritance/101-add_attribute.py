#!/usr/bin/python3
"""
add_attribute function

Adds a new attribute to an object if the object
allows dynamic attribute creation.

"""


def add_attribute(obj, attribute, value):
    """
    Args:
        obj (object): The object to which the attribute will be added.
        attribute (str): The name of the attribute to be added.
        value: The value to be assigned to the new attribute.

    Raises:
        TypeError: If the object does not allow dynamic attribute creation,
        either by having no '__dict__' attribute or having '__slots__'.
    """
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    if '__slots__' in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
