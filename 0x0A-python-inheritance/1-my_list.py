#!/usr/bin/python3
"""1-my_list.py"""


class MyList(list):
    """class MyList that inherits from list."""

    def print_sorted(self):
        """Prints the list in sorted order (ascending)."""
        sorted_list = sorted(self)
        print(sorted_list)
