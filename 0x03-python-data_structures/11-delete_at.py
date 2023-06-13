#!/usr/bin/python3
# 11-delete_at.py
def delete_at(my_list=[], idx=0):
    """Delete an item at a specific position in a list."""
    x = len(my_list)
    if idx < 0 or idx > (x - 1):
        return (my_list)
    for i in range(idx, x - 1):
        temp = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = temp
    del my_list[-1]
    return (my_list)
