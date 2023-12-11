#!/usr/bin/python3

""" Square class inherits from Rectangle class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square class.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square's position (default is 0).
            y (int): The y-coordinate of the square's position (default is 0).
            id (int): The identifier for the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter method for the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for the size of the square.

        Args:
            value (int): The new size of the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes of the Square.

        Args:
            *args: Variable number of arguments. Order: [id, size, x, y]
            **kwargs: Variable keyword arguments for
                        updating specific attributes.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the Square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
