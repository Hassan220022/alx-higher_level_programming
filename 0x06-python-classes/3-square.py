#!/usr/bin/python3
"""Class that defines a square"""


class Square:

    """Class that represents a square."""
    def __init__(self, size=0):
        """
        Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):

        """
        Return the current area of the square.
        """
        return self.__size * self.__size
