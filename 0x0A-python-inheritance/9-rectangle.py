#!/usr/bin/python3

"""
class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not a positive integer.
        """
        BaseGeometry.integer_validator(self, 'height', height)
        self.__width = width
        BaseGeometry.integer_validator(self, 'width', width)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
