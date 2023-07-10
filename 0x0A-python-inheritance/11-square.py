#!/usr/bin/python3
"""11-square.py"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Instantiation with size: def __init__(self, size):"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Return [Square] <width>/<height>"""
        return "[Square] {}/{}".format(self.__size, self.__size)
