#!/usr/bin/python3
"""A function that returns True if obect is and instance
of or if the object is an instance of a class that
nherited from, the specified class and False otherwise.
"""

def is_kind_of_class(obj, a_class):
    """Returns True if obj is and instace of a_class
    Argument:
        obj: The object to be compared 
        a_class: The class to be compared against
    """
    if isinstance(obj, a_class):
        return True
    return False
