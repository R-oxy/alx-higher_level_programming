#!/usr/bin/python3
"""Module that defines a function taht prints a square."""


def print_square(size):
    """Functions that prints an square with the # character.
    Args:
        size(int)
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
