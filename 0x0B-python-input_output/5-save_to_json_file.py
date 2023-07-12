#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def save_to_json_file(my_obj, filename):
    """Return the JSON representation of a string object."""
    myjson = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as myfile:
        myfile.write(myjson)
