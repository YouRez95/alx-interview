#!/usr/bin/python3

'''
    nqueens problem: (backtracking)
        find_solution(board, row, solutions):
            check if we reach the end of board
                true -> print solutions
                false -> continue
            Iterate throgh each row and run find_soltions
            recursively one function for each row:
                if we find a valid place append the place to the solutions
                else means we dont find any place for that specific row
                    pop the last soltions and continue to find another place
'''


import sys


def find_solutions(board, row, solutions) -> None:
    '''
        board: num of board
        row: start with 0
        solutions: list of solutions
    '''
    if row == board:
        print(solutions)
        return

    for col in range(board):
        if is_valid(row, col, solutions):
            solutions.append([row, col])
            find_solutions(board, row + 1, solutions)
            solutions.pop()


def is_valid(row, col, solutions) -> bool:
    '''
        check the validity of place:
            [0, 1] and [1, 2] is a wrong place for the second item
                checking for the diagonale is abs(0 - 1) == abs(1 - 2)
            [0, 0] and [1, 0] is a wrong place is align verticaly
                checking is compare each previous col by current col
    '''
    for r, c in solutions:
        if col == c or abs(r - row) == abs(c - col):
            return False
    return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)

    try:
        board = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if board < 4:
        print('N must be at least 4')
        exit(1)

    solutions = []
    find_solutions(board, 0, solutions)
