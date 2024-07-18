#!/usr/bin/python3
"""
Method module
"""


def inherits_from(obj, a_class):
    """check if object is an instance of a class
    args:
        obj: object to check
        a_class: class to check
    returns:
        True or False
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
