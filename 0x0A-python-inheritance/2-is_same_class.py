#!/usr/bin/python3
"""Defines an instance checking function"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a given class
    Arguments:
        obj(any): The object to check.
        a_class(type): The class to match the type of the obj
    Returns:
        True if obj is exactly an instance of a_class
        False: otherwise
    """
    if type(obj) == a_class:
        return True
    else:
        return False
