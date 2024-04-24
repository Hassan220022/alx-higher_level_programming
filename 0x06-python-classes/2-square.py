#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """
        Initialize a new Square with optional size.
        
        Args:
            size (int): The size of the new square, must be an integer
                        and must be greater than or equal to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
