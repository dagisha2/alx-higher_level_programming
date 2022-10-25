#!/usr/bin/python3
"""This module creates class and initiates object"""


class Square:
    """A class named Square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """GETTER"""
        return self.__size

    @size.setter
    def size(self, value):
        """SETTER"""
        try:
            if not isinstance(value, int):
                raise TypeError
            elif int(value) < 0:
                raise ValueError
            else:
                self.__size = value
        except TypeError as te:
            raise Exception("size must be an integer")
        except ValueError as ve:
            raise Exception("size must be >= 0")

    def area(self):
        """This method returns area of Square"""
        return self.__size * self.__size

    def my_print(self):
        """This method prints square with the character #"""
        if self.__size == 0:
            print()
        i = 0
        j = 0
        while (i < self.__size):
            while(j <= self.__size - 1):
                print(self.__size * chr(35))
                j += 1
            i += 1
        print()
