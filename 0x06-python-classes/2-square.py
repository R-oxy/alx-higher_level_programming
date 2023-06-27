#!/usr/bin/python3
"""define a class square"""

class Square:
    def __init__(self, size = 0):
        """

        Initializes a square with the given size.

        Args:
            size (int): size of the square, default 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
