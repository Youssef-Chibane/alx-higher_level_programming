#!/usr/bin/python3

"""
MyInt class, a subclass of int.

This class overrides the equality (__eq__) and inequality (__ne__) methods
to provide custom behavior for comparing MyInt objects with other integers.

Methods:
     __eq__(self, other):
        Compares the value of MyInt with another integer
        using a non-standard equality check.

    __ne__(self, other):
        Compares the value of MyInt with another integer
        using a non-standard inequality check.
"""


class MyInt(int):
    def __eq__(self, other):
        return int(str(self)) != other

    def __ne__(self, other):
        return int(str(self)) == other
