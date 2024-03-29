#!/usr/bin/python3

"""class rectangle"""


class Rectangle:
    """rectangle"""

    def __init__(self, width=0, height=0):
        """initiaze new rectangle
        Args:
           width: width of rectangle
           height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve the width of rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve the height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter of square"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        reclist = []
        for i in range(self.__height):
            [reclist.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                reclist.append("\n")
        return ("".join(reclist))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        reclist = "Rectangle(" + str(self.__width)
        reclist += ", " + str(self.__height) + ")"
        return (reclist)
