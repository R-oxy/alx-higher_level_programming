#!/usr/bin/python3
"""100-my_int.py"""

class MyInt(int):
    """A class Int that inherits from int"""

    def __eq__(self, value):
        """Overrides __eq__ method(==) to __ne__ method(!=)"""
        return super().__ne__(value)

    def __ne__(self, value):
        """Overrides __ne__ method(!=) to __eq__ method(==)"""
        return super().__eq__(value)
