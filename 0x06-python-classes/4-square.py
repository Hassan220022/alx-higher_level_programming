#!/usr/bin/python3
"""Class that defines a square with private instance attribute size and public instance method area."""

class Square:
    """Class that defines a square.
    
    Attributes:
        size (int): The size of a side of the square.
    """
    
    def __init__(self, size=0):
        """Initialize a new Square with optional size.
        
        Args:
            size (int): The size of a side of the square (default is 0).
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # Calls the setter below

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.
        
        Args:
            value (int): The new size of the square.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
