#!/usr/bin/python3
"""
function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """matrix must be a list of lists of integers or floats
    Each row of the matrix must be of the same size
    div must be a number (integer or float),
    div can’t be equal to 0
    """
    correct_input = True

    if not isinstance(matrix, list):
        correct_input = False

    for sublist in matrix:
        if not isinstance(sublist, list):
            correct_input = False
            break
        for elem in sublist:
            if not isinstance(elem, (int, float)):
                correct_input = False

    if not correct_input:
        raise TypeError(
            'matrix must be a matrix (list of lists)'
            ' of integers/floats'
            )

    for sublist in matrix:
        if len(sublist) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError()
    if div == 0:
        raise ZeroDivisionError('division by zero')

    matrix_final = []

    for sublist in matrix:
        matrix_final.append(list(map(lambda x: round(x / div, 2), sublist)))
    return matrix_final
