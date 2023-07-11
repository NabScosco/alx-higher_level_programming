#!/usr/bin/python3
"""This is a  function that defines an inherited list"""


class MyList(list):
    """Returns a sorted list"""

    def print_sorted(self):
        print(sorted(self))
