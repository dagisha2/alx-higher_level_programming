#!/usr/bin/python3
"""This module creates class and initiates object"""


class Square:

    """This is class named Square"""
    def __init__(self, size=None):
        if size < 0:
            raise ValueError("size must be >= 0")
        elif size != int:
            raise TypeError("size must be an integer")
        self.__size = size
