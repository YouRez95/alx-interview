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
    should_break = False

    for i, row in enumerate(grid):
        if should_break:
            break
        for j, col in enumerate(row):
            if col == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 1
                if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
            if perimeter == 4:
                should_break = True
                break
    return perimeter
