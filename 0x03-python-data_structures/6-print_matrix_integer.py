#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        x = len(row) - 1
        y = 0
        for col in row:
            print("{:d}".format(col), end=" " if y != x else "")
            y += 1
        print()
