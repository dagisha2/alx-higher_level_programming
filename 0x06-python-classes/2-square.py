#!/usr/bin/python3
"""This module creates class and initiates object"""


class Square:
    """This is class named Square"""
    def __init__(self, size=0):
        try:
            if int(size) < 0:
                raise ValueError
            elif not isinstance(size, int):
                raise TypeError
            else:
                self.__size = size
        except ValueError as ve:
            raise Exception("size must be >= 0")
        except TypeError as te:
            raise Exception("size must be an integer")
