#!/usr/bin/python3
"""
    rotate 2D matrix
"""


def rotate_2d_matrix(matrix):
    '''
        rotate 2D matrix
    '''
    new_matrix = []
    for row in matrix:
        for index, item in enumerate(row):
            try:
                new_matrix[index].append(item)
            except IndexError:
                new_matrix.append([item])
    for index, row in enumerate(new_matrix):
        row.reverse()
        matrix[index] = row
