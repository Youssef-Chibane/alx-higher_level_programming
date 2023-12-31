#!/usr/bin/python3
"""
mylist.py - A Python script defining a custom
class 'MyList' that extends the built-in 'list' class.

"""


class MyList(list):
    """
    A custom class that extends the built-in 'list' class.

    """
    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.
        """
        print(sorted(self))
