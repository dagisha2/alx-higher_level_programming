#!/usr/bin/python3
"""This module creates empty class"""


class Rectangle:
    """This is a class named Rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        try:
            if not isinstance(value, int):
                raise TypeError
            elif value < 0:
                raise ValueError
            else:
                self.__width = value
        except TypeError as te:
            raise Exception("width must be an integer")
        except ValueError as ve:
            raise Exception("width must be >= 0")

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        try:
            if not isinstance(value, int):
                raise TypeError
            elif value < 0:
                raise ValueError
            else:
                self.__height = value
        except TypeError as te:
            raise Exception("height must be an integer")
        except ValueError as ve:
            raise Exception("height must be >= 0")
