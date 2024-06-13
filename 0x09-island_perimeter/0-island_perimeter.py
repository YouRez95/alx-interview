#!/usr/bin/python3
"""
    0. Island Perimeter
"""


def island_perimeter(grid):
    '''
        function that returns the perimeter
        of the island described in grid
    '''
    perimeter = 0

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == 1:
                perimeter += 4
                if grid[i - 1][j] == 1:
                    perimeter -= 1
                if grid[i][j-1] == 1:
                    perimeter -= 1
                if grid[i][j + 1] == 1:
                    perimeter -= 1
                if grid[i + 1][j] == 1:
                    perimeter -= 1
    return perimeter
