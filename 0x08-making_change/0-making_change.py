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
    
    # Initialize dp array with infinity for all amounts except 0
    # dp[i] represents minimum coins needed to make amount i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins needed to make amount 0
    
    # For each amount from 1 to total
    for amount in range(1, total + 1):
        # Try each coin denomination
        for coin in coins:
            # If coin value is not greater than current amount
            if coin <= amount:
                # Update minimum coins needed for current amount
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # If dp[total] is still infinity, total cannot be made
    return dp[total] if dp[total] != float('inf') else -1
