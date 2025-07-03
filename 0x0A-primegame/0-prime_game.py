#!/usr/bin/python3

"""
Prime Game

This module contains the logic to simulate the Prime Game, where two players take turns removing primes and their multiples from a sequence of integers.
"""

def sieve_of_eratosthenes(limit):
    """
    Implements the Sieve of Eratosthenes to find all prime numbers up to a given limit.

    Args:
        limit (int): The upper bound of the range to find primes.

    Returns:
        list: A list of prime numbers up to the specified limit.
    """
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False  # 0 and 1 are not primes
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return [i for i in range(2, limit + 1) if primes[i]]

def isWinner(x, nums):
    """
    Determines the winner of the Prime Game based on multiple rounds.

    Args:
        x (int): The number of rounds to play.
        nums (list of int): A list of integers, each representing the upper bound of the range for a game.

    Returns:
        str: The name of the player who won the most rounds, or None if it's a tie.
    """
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    prime_set = set(primes)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count how many primes are there up to n
        count_primes = sum(1 for p in prime_set if p <= n)

        # Maria goes first, if the number of primes is odd, Maria wins, else Ben wins
        if count_primes % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(3, [4, 5, 1])))
