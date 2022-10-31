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

    def area(self):
        """this method returns area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """this method returns perimeter of the rectangle"""
        if self.__width == 0:
            return 0
        elif self.__height == 0:
            return 0
        else:
            return 2 * self.__width + 2 * self.__height

    def pprint(self):
        """this method returns rectangle with # in string form"""
        height = self.__height
        width = self.__width
        return '\n'.join('#' * width for _ in range(height))

    def __str__(self):
        """Instance method that returns an
        “informal” and nicely printable string
        representation of an instance
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return f"{self.pprint()}"

    def __repr__(self):
        """Instance method that returns an“official” string representation
        of an instance
        """
        rep = 'Rectangle(' + str(self.__width) + \
              ','' ' + str(self.__height) + ')'
        return rep

    def __del__(self):
        """Instance method called when object is deleted"""
        print("Bye rectangle...")
