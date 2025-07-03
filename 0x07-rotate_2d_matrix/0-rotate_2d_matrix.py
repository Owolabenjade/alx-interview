#!/usr/bin/python3
"""
Module for rotating a 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate an n x n 2D matrix 90 degrees clockwise in-place.

    The algorithm works in two steps:
    1. Transpose the matrix (swap rows and columns)
    2. Reverse each row

    Args:
        matrix (list of lists): n x n 2D matrix to rotate

    Returns:
        None: The matrix is modified in-place

    Example:
        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> rotate_2d_matrix(matrix)
        >>> print(matrix)
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    """
    n = len(matrix)

    # Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i])
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
