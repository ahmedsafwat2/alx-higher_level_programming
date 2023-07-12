#!/usr/bin/python3
def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, mode = "r", encoding = "utf-8") as myfile:
        print(myfile.read(),end = "")
