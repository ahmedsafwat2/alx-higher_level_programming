#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def save_to_json_file(my_obj, filename):
    """Return the JSON representation of a string object."""
    with open(filename, "w") as myfile:
        json.dump(my_obj, myfile)
