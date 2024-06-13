#!/usr/bin/python3
"""
    0. Island Perimeter
"""


def island_perimeter(grid):
    '''
        function that returns the perimeter
        of the island described in grid
    '''
    land = []
    perimeter = 0
    for row in grid:
        for col in row:
            if col == 1:
                land.append(1)
    if len(land) == 1:
        return 4
    for i in range(0, len(land)):
        if i == 0 or i == len(land) - 1:
            perimeter += 3
        else:
            perimeter += 2
    return perimeter