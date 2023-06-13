#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    x = len(my_list)
    if x == 0:
        return (None)
    maxi = my_list[0]
    for i in range(1, x):
        if my_list[i] > maxi:
            maxi = my_list[i]
    return (maxi)
