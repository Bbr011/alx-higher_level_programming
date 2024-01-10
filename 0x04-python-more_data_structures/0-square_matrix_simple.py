#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return (list (map (lambda squar_matrix: list (map (lambda i: i**2, squar_matrix)), matrix)))
