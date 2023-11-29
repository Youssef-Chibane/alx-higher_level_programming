#!/usr/bin/python3

def matrix_divided(matrix, div):
    """

    Divides all elements of a matrix by a given divisor.

    Args:
    - matrix (list of lists): The matrix to be divided.
    - div (int or float): The divisor.

    Returns:
    - list of lists: A new matrix where each element
    is the result of the division.

    Raises:
    - TypeError: If the divisor is not a number,
    if the matrix is not a list of lists,
    or if the elements within the matrix are not integers or floats.
    - ZeroDivisionError: If the divisor is zero.
    - TypeError: If the rows of the matrix do not have the same size.

    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    error_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(error_type)

    len_e = 0
    error_size = "Each row of the matrix must have the same size"

    for elements in matrix:
        if not elements or not isinstance(elements, list):
            raise TypeError(error_type)

        if len_e != 0 and len(elements) != len_e:
            raise TypeError(error_size)

        for num in elements:
            if not isinstance(num, (int, float)):
                raise TypeError(error_type)

        len_e = len(elements)

    result = list(map(lambda x: list(map(lambda y:
                                         round(y / div, 2), x)), matrix))

    return result
