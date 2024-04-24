#!/usr/bin/python3
"""Class that defines a square"""

class Square:
    """Class that defines a square by: (based on 1-square.py)."""

    def __init__(self, size=0):
        """Initialize Square instance with size"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
