#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if not isinstance(my_list, list):
        print("Invalid argument. Expected a list.")
        return

    reversed_list = my_list[::-1]
    for element in reversed_list:
        print("{:d}".format(element))
