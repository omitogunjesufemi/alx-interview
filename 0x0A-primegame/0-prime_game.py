#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of consecutive integers
starting from 1 up to and including `n`, they take turns choosing a prime
number from the set and removing that number and its multiples from the
set. The player that cannot make a move loses the game.

They play `x` rounds of the game, where `n` may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.
"""


def isWinner(x, nums):
    """
    `x` is the number of rounds
    `nums` is an array of `n`

    Return: name of the player that won the most rounds
    If the winner cannot be determined, return `None`
    """
    """
    if len(nums) <= 0 or x <= 0:
        return None

    move_list = []
    for num in nums:
        num_list = [k for k in range(1, num + 1)]
        starting_point = 1

        count = 0
        while (starting_point < len(num_list)):
            div = num_list[starting_point]
            to_be_rmvd = [k for k in num_list if k % div == 0]

            for i in to_be_rmvd:
                num_list.remove(i)

            count += 1
            if len(num_list) == 1:
                break
        move_list.append(count)

    even = 0
    odd = 0
    for move in move_list:
        if move % 2 == 0:
            even += 1
        else:
            odd += 1

    if even > odd:
        return "Ben"
    elif odd > even:
        return "Maria"

    return None
    """

    if x <= 0 or len(nums) == 0:
        return None

    max_n = max(nums)

    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    primes_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        primes_count[i] = primes_count[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
