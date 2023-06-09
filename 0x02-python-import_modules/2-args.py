#!/usr/bin/python3

if __name__ == "_main_":

    from sys import argv

    num_args = len(argv) - 1

    print(f"{num_args} {'argument' if num_args == 1\
            else 'arguments'}{'.' if num_args == 0 else ':'}")

    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
