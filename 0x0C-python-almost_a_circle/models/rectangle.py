#!/usr/bin/python3
"""Define a Rectangle class."""
from models.base import Base


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
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return
        mylist = []
        for i in range(self.y):
            mylist.append("\n")
        for i in range(self.height):
            for j in range(self.x):
                mylist.append(" ")
            for h in range(self.width):
                mylist.append("#")
            mylist.append("\n")
        print("".join(mylist), end="")

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        mystr = ""
        mystr = "[Rectangle] (" + str(self.id) + ") "
        mystr += str(self.x) + "/" + str(self.y)
        mystr += " - " + str(self.width) + "/" + str(self.height)
        return mystr
