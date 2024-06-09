#!/usr/bin/python3

'''
    Given a pile of coins of different values
    determine the fewest number of coins needed
    to meet a given amount total
'''


def count(coins, sum, total, result):
    '''
        recursive function will called until meet the total
        or the coins is empty list
    '''
    if len(coins) == 0:
        return
    largest_num = coins[-1]
    if sum + largest_num < total:
        sum += largest_num
        result.append(largest_num)
    elif sum + largest_num > total:
        coins.pop()
    else:
        sum += largest_num
        result.append(largest_num)
        return result
    count(coins, sum, total, result)


def makeChange(coins, total):
    '''
        entry of the problem
        will check the result if has sum is equal total
        then we return the len(result) which is the total of coins
        else -1
    '''
    if total <= 0:
        return 0
    if len(coins) == 0:
        return 0
    start_sum = 0
    result = []
    coins.sort()
    count(coins, start_sum, total, result)
    final_sum = sum(result)
    return len(result) if final_sum == total else -1
