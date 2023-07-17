#!/usr/bin/python3
"""Define a Rectangle class."""
from base import Base


class Rectangle(Base):
    """Represent a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
    self.value_validation("width", width)
    self.__width = width
    self.value_validation("height", height)
    self.__height = height
    self.x_y_validation("x", x)
    self.__x = x
    self.x_y_validation("y", y)
    self.__y = y
    super().__init__(id)

