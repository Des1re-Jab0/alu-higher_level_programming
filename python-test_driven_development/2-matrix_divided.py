#!/usr/bin/python3
"""Module that divides a matrix by a given number.

Defines matrix_divided, which returns a new matrix with every
element divided by div, rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div, rounded to 2 decimals.

    Validates that matrix is a list of lists of numbers with equal
    row sizes, and that div is a nonzero number.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of "
                    "integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(n / div, 2) for n in row] for row in matrix]
