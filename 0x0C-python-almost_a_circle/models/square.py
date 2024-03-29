#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.__width

    @size.setter
    def size(self, value):
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Update the Square.
        Args:
            *args (ints): New attribute values.
            - 1st argument represents id attribute
            - 2nd argument represents size attribute
            - 3rd argument represents x attribute
            - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        a = 0
        for arg in args:
            if a == 0:
                self.id = arg
            elif a == 1:
                self.size = arg
            elif a == 2:
                self.x = arg
            elif a == 3:
                self.y = arg
            a += 1
        for k, v in kwargs.items():
            if k == "id":
                self.id = v
            elif k == "size":
                self.size = v
            elif k == "x":
                self.x = v
            elif k == "y":
                self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        mystr = ""
        mystr = "[Square] (" + str(self.id) + ") "
        mystr += str(self.x) + "/" + str(self.y)
        mystr += " - " + str(self.size)
        return mystr
