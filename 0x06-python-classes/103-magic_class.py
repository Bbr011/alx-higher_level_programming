#!/usr/bin/python3

"""MagicClass matching exactly a bytecode provided by Holberton."""

import math


class MagicClass:
    """a circle."""

    def __init__(self, radius=0):
        """MagicClass.

        Arg:
            radius (float or int): radius of new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return area of MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return circumference of MagicClass."""
        return (2 * math.pi * self.__radius)
