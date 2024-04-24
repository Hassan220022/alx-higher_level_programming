#!/usr/bin/python3
"""Class that defines a square"""


class Square:
    """
    Class that defines a square by: (based on 1-square.py).
    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0):
        """Initialize Square instance with size
        args:
            size: size of a square (1 side).
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
