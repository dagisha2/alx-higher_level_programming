#!/usr/bin/python3
"""This module creates empty class"""


class Rectangle:
    """This is a class named Rectangle"""
    def __init__(self, width=0, height=0):
        """this constructs  object"""

        self.height = height
        self.width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif int(value) < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif int(value) < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
