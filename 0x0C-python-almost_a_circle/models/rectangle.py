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
