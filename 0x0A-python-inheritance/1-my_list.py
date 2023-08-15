#!/usr/bin/python3
"""
Contains class MyList
inherits from list; has public instance method to print sorted
"""


class MyList(list):
    """inherits from list
    """
    def print_sorted(self):
        """prints list of ints all sorted in ascending order"""
        print(sorted(self))
"""print_sorted - method to sort a list"""
        l = (sorted(self[:]))
        print(l)
