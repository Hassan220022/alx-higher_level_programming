#!/usr/bin/python3
"""
class module
"""


class BaseGeometry:
    """Geometry class"""

    def area(self):
        """raise exception is area is not implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """check if value is an integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
