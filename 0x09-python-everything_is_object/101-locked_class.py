#!/usr/bin/python3
"""Module that defines a locked class"""


class LockedClass:
    """allows ONLY first_name attribute"""
    __slots__ = ['first_name']
