#!/usr/bin/python3
"""This module creates class and initiates object"""


class Square:

    """This is class named Square"""
    def __init__(self, size=0):
        try:
            if int(size) < 0:
                raise ValueError("size must be >= 0")
            elif not isinstance(size, int):
                raise TypeError("size must be an integer")
            else:
                self.__size = size
        except(ValueError, TypeError) as size:
            print("{}".format(size))
