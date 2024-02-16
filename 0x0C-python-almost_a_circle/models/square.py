#!/usr/bin/python3
"""modules imported"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize a new square
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        self.__width = value
        self.__height = value
