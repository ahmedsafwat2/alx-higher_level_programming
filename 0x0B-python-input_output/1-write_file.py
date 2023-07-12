#!/usr/bin/python3
"""Define writing function"""
def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.
    Args:
        filename(str): name of file to write.
        text(str): text be written.
        Returns:
            number refer to character written.
    """
    with open(filename, "w") as myfile:
        return (myfile.write(text))
