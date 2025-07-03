#!/usr/bin/python3

"""
Prime Game

This module contains the logic to simulate the Prime Game,
where two players take turns removing primes
and their multiples from a sequence of integers.
"""


def sieve_of_eratosthenes(limit):
    """
    Implements the Sieve of Eratosthenes
    to find all prime numbers up to a given limit.

    Args:
        limit (int): The upper bound of the range to find primes.

    Returns:
        list: A list of prime numbers up to the specified limit.
    """
    if limit <= 1:
        return []  # No primes if limit is less than 2

    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False  # 0 and 1 are not primes
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return [i for i in range(2, limit + 1) if primes[i]]


def simulate_game(n):
    """
    Simulates a single game and determines the winner.
    
    Args:
        n (int): The upper bound of numbers available (1 to n)
    
    Returns:
        str: "Maria" if Maria wins, "Ben" if Ben wins
    """
    if n <= 1:
        return "Ben"  # No primes available, Ben wins by default
    
    # Get all primes up to n
    primes = sieve_of_eratosthenes(n)
    
    # Track available numbers
    available = [True] * (n + 1)
    available[0] = False  # 0 is not in the game
    
    moves = 0
    
    # Simulate the game
    while True:
        # Find the smallest available prime
        prime_chosen = None
        for prime in primes:
            if prime <= n and available[prime]:
                prime_chosen = prime
                break
        
        # If no prime is available, current player loses
        if prime_chosen is None:
            break
        
        # Remove the prime and all its multiples
        for i in range(prime_chosen, n + 1, prime_chosen):
            available[i] = False
        
        moves += 1
    
    # Maria goes first, so if moves is odd
    # Maria made the last move and wins
    return "Maria" if moves % 2 == 1 else "Ben"


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game
    based on multiple rounds.

    Args:
        x (int): The number of rounds to play.
        nums (list of int): A list of integers,
        each representing the upper bound of the range for a game.

    Returns:
        str: The name of the player who
        won the most rounds, or None if it's a tie.
    """
    if x <= 0 or not nums:
        return None  # No rounds to play or invalid input
    
    # Only consider the first x rounds
    rounds_to_play = nums[:x]
    
    maria_wins = 0
    ben_wins = 0

    for n in rounds_to_play:
        winner = simulate_game(n)
        if winner == "Maria":
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
    print("Winner: {}".format(isWinner(5, [1, 2, 3, 4, 5])))
    print("Winner: {}".format(isWinner(1, [1])))
    print("Winner: {}".format(isWinner(-1, [10])))
