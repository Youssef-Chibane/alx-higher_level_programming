#!/usr/bin/python3
"""
basegeometry.py - A Python script defining a base class
'BaseGeometry' for geometry-related functionality.

"""


class BaseGeometry:
    """
    A base class for geometry-related functionality.

    """
    def area(self):
        """
        Raises an exception indicating that 'area' is not implemented.

        This method should be implemented by subclasses
        to provide specific area calculation.

        Raises:
            Exception: Indicates that 'area' is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the input value is an integer and greater than 0.

        Parameters:
            - name (str): The name of the variable being validated.
            - value: The value to be validated.

        Raises:
            - TypeError: If the value is not an integer.
            - ValueError: If the value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
