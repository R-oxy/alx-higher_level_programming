#!/usr/bin/python3
"""100-append_after.py"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line
    containing a specific string (see example)
    """
    txt = ""
    with open(filename) as file:
        for line in file:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as a_file:
        a_file.write(txt)
