#!/usr/bin/python3
"""square class inherits for rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents a square using Rectangle"""
    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size". size)
        super().__init__(size, size)
        self.size = size
