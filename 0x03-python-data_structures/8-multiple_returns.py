#!/usr/bin/python3
# 8-multiple_returns.py
def multiple_returns(sentence):
    """Returns the length of a string and its first character."""
    x = len(sentence)
    if x == 0:
        return (0, None)
    else:
        return (x, sentence[0])
