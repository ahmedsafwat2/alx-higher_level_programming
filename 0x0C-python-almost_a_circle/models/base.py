#!/usr/bin/python3
"""Define a base module class"""


class Base:
    """create a Base class.
    private class Attributes:
         __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):

        """ Initiate a new Base.
        Args:
            id(int): the identity of new base.
        """
        if id not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
        def value_validation(self, name, value):
            if type(value) is not int:
                raise TypeError(f"{name} must be an integer")
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
        def x_y_validation(self, name, value):
            if value < 0:
                raise ValueError(f"{name} must be >= 0")
