#!/usr/bin/python3
"""
Class module.
"""

class MyInt(int):
    """Class with int object"""

    def __eq__(self, other):
        """Equal equal method"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Not equal method"""
        return super().__eq__(other)
