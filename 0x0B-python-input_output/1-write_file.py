#!/usr/bin/python3
'''task 1 module'''


def write_file(filename="", text=""):
    """writes to text file and retunrs num chars written"""
    with open(filename, 'w', encoding="utf-8") as f:
        return(f.write(text))
