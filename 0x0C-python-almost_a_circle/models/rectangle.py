#!/usr/bin/python3
"""modules"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """rectangle initialization
        Args:
            width (int): width of Rectangle.
            height (int): height of Rectangle.
            x (int): x coordinate of Rectangle.
            y (int): y coordinate of Rectangle.
            id (int): identity of Rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''Width of this rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''Height of this rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''x of this rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        '''y of this rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value
