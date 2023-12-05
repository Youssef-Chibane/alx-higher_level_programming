#!/usr/bin/python3

"""
Module: 10-square
------------------

This module defines a class Square that inherits from the Rectangle class.
"""

# Importing the Rectangle class from the 9-rectangle module
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class, a subclass of Rectangle.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with the given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not a positive integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
