#!/usr/bin/python3
"""Module that defines a function that prints an indented text"""


def text_indentation(text):
    """Prints a text with 2 new lines after '.', '?', and ':'.
    Args:
        text (string)
    Raises:
        TypeError: If text is not a string.
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    punctuation = [".", "?", ":"]
    new_text = ""
    for char in text:
        new_text += char
        if char in punctuation:
            new_text += "\n\n"

    print(new_text.rstrip())
