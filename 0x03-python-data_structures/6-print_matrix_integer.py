#!/bin/paython3
def print_matrix_integer(matrix=[[]]):
    '''print all integers'''
    for i in matrix:
        x = len(i) - 1
        y = 0
        for j in i:
            print("{:d}".format(j), end=" " if y != x else "")
            y += 1
        print()
