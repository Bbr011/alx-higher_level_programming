#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squar_matrix = matrix[:]
    for i in matrix:
        for j in matrix:
            squar_matrix[i][j] = matrix[i][j] ** 2
    return (squar_matrix)
