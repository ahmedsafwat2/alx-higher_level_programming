#!/usr/bin/python3
class Square:
     """Represent a class square."""
    def __init__ (self, size = 0):
          """Initialize a new square.

        Args:
            size (int): The size of the new squre
            """
        self.__size = size
    @property
    def size (self):
        return (self.__size)
    @size.sitter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

