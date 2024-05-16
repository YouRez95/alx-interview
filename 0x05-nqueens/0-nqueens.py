#!/usr/bin/python3

'''
    Task:
        n queens
'''

import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

board = sys.argv[1]

try:
    board = int(board)
except ValueError:
    print('N must be a number')
    exit(1)

if board < 4:
    print('N must be at least 4')
    exit(1)


path = [[0, 0]]


def find_solutions(i, j, board):
    '''
        n queens by backtracking
    '''
    if i == board:
        return
    if j == board:
        last_track = path.pop()
        i = last_track[0]
        j = last_track[1] + 1
    path.append([i, j])
    if (path[len(path) - 1][1] == path[len(path) - 2][1]
        or
            (path[len(path) - 2][0] + 1 == path[len(path) - 1][0]
             and path[len(path) - 2][1] + 1 == path[len(path) - 1][1])
        or
            (path[len(path) - 2][0] + 1 == path[len(path) - 1][0]
             and path[len(path) - 2][1] - 1 == path[len(path) - 1][1])):
        path.pop()
    else:
        i += 1
        j = -1
    find_solutions(i, j + 1, board)
    print(path)


find_solutions(1, 0, board)
