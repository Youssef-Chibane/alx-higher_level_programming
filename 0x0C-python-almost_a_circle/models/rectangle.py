#!/usr/bin/python3
"""
Module that defines a class Rectangle, which inherits from the Base class.

"""

from models.base import Base


class Rectangle(Base):
    """
    Defines a Rectangle class that represents a rectangle
    with width, height, x-coordinate, y-coordinate,
    and an optional identifier (id).
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
            id (int): An optional identifier for the rectangle.

        Raises:
            TypeError: If width, height, x, or y is not an integer.
            ValueError: If width, height, x, or y has an invalid value.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x-coordinate of the rectangle's upper-left corner."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x-coordinate of the rectangle's upper-left corner."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y-coordinate of the rectangle's upper-left corner."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y-coordinate of the rectangle's upper-left corner."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
