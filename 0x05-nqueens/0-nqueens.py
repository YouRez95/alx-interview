#!/usr/bin/python3
'''
    Task:
        n queens
'''

import sys
import math

sys.setrecursionlimit(5000)

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


def find_solutions(row, col, solutions):

    '''
        n-queens problem
    '''
    if row == board:
        return

    new_place = valid_place(row, col, solutions)
    # print("valid: ", new_place)
    if new_place:
        solutions.append(new_place)
        # print("add", solutions)
        if len(solutions) == board:
            print(solutions)
            last_path = solutions.pop()
            find_solutions(last_path[0], last_path[1] + 1, solutions)
        else:
            find_solutions(row + 1, 0, solutions)
    else:
        if len(solutions) == 0:
            return
        last_path = solutions.pop()
        # print("remove", solutions)
        find_solutions(last_path[0], last_path[1] + 1, solutions)


def valid_place(row, col, solutions):
    '''
        return the valid place
        else False
    '''
    if col == board:
        return False

    if is_valid(row, col, solutions):
        return [row, col]

    result = valid_place(row, col + 1, solutions)
    if result is not False:
        return result

    return False


def is_valid(row, col, solutions):
    '''
        check if is valid place
    '''
    for path in solutions:
        if path[1] == col or abs(path[0] - row) == abs(path[1] - col):
            return False
    return True


solutions = []
find_solutions(0, 0, solutions)
