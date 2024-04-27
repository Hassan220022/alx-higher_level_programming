#!/usr/bin/python3
"""
This module defines a function add_integer that adds two integers.
The function ensures that the inputs are either integers or floats,
casting floats to integers before performing the addition.
"""


def add_integer(a, b=98):
    """Return the addition of a and b, or errors if input types are invalid."""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
