#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet total
    - if total is 0 or less, return 0
    - if total cannot be met by any number of coins, return -1

    The coins is a list of the values of coins in possession
    The value of a coin will always be > 0
    """

    """Sorting in descending order """
    if total == 0:
        return 0

    if len(coins) == 0:
        return -1

    min_num_of_coins = 0
    coins.sort(reverse=True)

    for coin in coins:
        if total == 0:
            return min_num_of_coins

        if coin <= total:
            num_of_coin = total // coin
            total = total - (num_of_coin * coin)
            min_num_of_coins += num_of_coin
    if total > 0:
        min_num_of_coins = -1

    return (min_num_of_coins)
