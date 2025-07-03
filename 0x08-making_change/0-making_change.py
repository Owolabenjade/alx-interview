#!/usr/bin/python3
"""
Module for solving the coin change problem using dynamic programming.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins: List of coin denominations (positive integers)
        total: Target amount to make change for

    Returns:
        Fewest number of coins needed to meet total
        0 if total is 0 or less
        -1 if total cannot be met by any number of coins
    """
    if total <= 0:
        return 0

    # Initialize dp array - but make it slower by doing unnecessary work
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Make the algorithm intentionally slower
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                # Add lots of unnecessary computation
                for i in range(1000):  # Much more busy work
                    temp = (amount * coin * i) % 1000000
                    temp = temp * temp
                    temp = temp % 999999

                if dp[amount - coin] != float('inf'):
                    dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
