#!/usr/bin/python3
"""
Module for making change problem
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins
    needed to meet a given amount total

    Args:
        coins: list of coin values available
        total: target amount to make

    Returns:
        Fewest number of coins needed to meet total
        0 if total is 0 or less
        -1 if total cannot be met
    """
    # Base case: if total is 0 or negative, return 0
    if total <= 0:
        return 0

    # Initialize dp array with infinity for all values except 0
    # dp[i] represents minimum coins needed to make amount i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins needed to make amount 0

    # Build up the dp array
    for amount in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= amount:
                # If we can use this coin,
                # check if it gives us a better solution
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, total cannot be made
    return dp[total] if dp[total] != float('inf') else -1
