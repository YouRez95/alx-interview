#!/usr/bin/python3

'''
Maria and Ben are playing a game. Given a set of consecutive
integers starting from 1 up to and including n, they take turns
choosing a prime number from the set and removing that number
and its multiples from the set.
The player that cannot make a move loses the game.
'''


def isPrime(n):
    '''
    check if the number is prime or not
    '''
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def removeMultiplesOfN(n, nums):
    '''
    remove multiples of number
    '''
    for num in nums:
        if num % n == 0:
            nums.remove(num)
    return nums


def isWinner(x, nums):
    '''
    play x rounds of the game, where n may be different
    for each round. Assuming Maria always goes first
    and both players play optimally, determine who the winner of each game is.
    x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    '''
    score = {'Maria': 0, 'Ben': 0}
    for num in nums:
        board = [i for i in range(1, num + 1)]
        if len(board) == 1 and board[0] == 1:
            score['Ben'] += 1
            continue
        i = 0
        winner = 'Ben'
        while i < len(board):
            num = board[i]
            if isPrime(num):
                if winner == 'Ben':
                    winner = 'Maria'
                else:
                    winner = 'Ben'
                board = removeMultiplesOfN(num, board)
            else:
                i += 1
        score[winner] += 1
    print(score)
    if score['Ben'] > score['Maria']:
        return 'Ben'
    elif score['Ben'] < score['Maria']:
        return 'Maria'
    else:
        return None
