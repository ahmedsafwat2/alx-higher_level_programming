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

    @property
    def width(self):
        """set/get the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.value_validation("width", value)
        self.__width = value

    @property
    def height(self):
        """set/get the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.value_validation("height", value)
        self.__height = value

    @property
    def x(self):
        """set/get the x of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.x_y_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """set/get the y of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.x_y_validation("y", value)
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        mylist = []
        for i in range(self.__y):
            mylist.append("\n")
        for i in range(self.__height):
            for j in range(self.__x):
                mylist.append(" ")
            for h in range(self.__width):
                mylist.append("#")
            mylist.append("\n")
        print("".join(mylist), end="")

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        mystr = ""
        mystr = "[Rectangle] (" + str(self.id) + ") "
        mystr += str(self.__x) + "/" + str(self.__y)
        mystr += " - " + str(self.__width) + "/" + str(self.__height)
        return mystr



