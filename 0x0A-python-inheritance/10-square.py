#!/usr/bin/python3
"""10-square.py"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square thst inherits from Rectangle"""

    def __init__(self, size):
        """Instantiation with size: def __init__(self, size):"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
