#!/usr/bin/python3
"""
Module for making change problem
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total

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

    # Quick check: if all coins are even and total is odd, impossible
    if all(coin % 2 == 0 for coin in coins) and total % 2 == 1:
        return -1

    # Remove duplicates and sort in descending order
    coins = sorted(set(coins), reverse=True)

    # Try greedy approach first for common cases
    if 1 in coins:
        # If we have a 1 coin, we can always make any amount
        # Try greedy first
        remaining = total
        count = 0
        for coin in coins:
            if coin <= remaining:
                count += remaining // coin
                remaining %= coin
        return count

    # For other cases, use optimized DP
    # Use a smaller range if possible
    max_coin = coins[0]

    # Initialize dp array
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    # Build up the dp array more efficiently
    for i in range(1, total + 1):
        for coin in coins:
            if coin > i:
                break
            if dp[i - coin] != total + 1:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
