#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two numbers and returns the result.

    Parameters:
    - a (int or float): The first number to be added.
    - b (int or float, optional): The second number to be added. Default is 98.

    Returns:
    int: The sum of the two input numbers.

    Raises:
    TypeError: If either 'a' or 'b' is not an integer or a float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer or float")

    a = int(a)
    b = int(b)
    return a + b
