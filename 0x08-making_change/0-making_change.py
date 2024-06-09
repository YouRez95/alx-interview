#!/usr/bin/python3

'''
    Given a pile of coins of different values
    determine the fewest number of coins needed
    to meet a given amount total
'''


def makeChange(coins, total):
    if total <= 0:
        return 0

    max_value = total + 1
    result = [max_value] * (total + 1)
    result[0] = 0
    for coin in coins:
        for x in range(coin, total + 1):
            result[x] = min(result[x], result[x - coin] + 1)

    return result[total] if result[total] != max_value else -1
