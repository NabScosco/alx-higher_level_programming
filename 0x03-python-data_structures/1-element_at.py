#!/usr/bin/python3

1def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return print("Eliment at index {:d} is {}".format(my_list[idx]))
