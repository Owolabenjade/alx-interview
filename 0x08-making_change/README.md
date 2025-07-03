# 0x08. Making Change

## Project Overview
This project implements a solution to the classic coin change problem using dynamic programming. The goal is to find the minimum number of coins required to make up a given total amount from a list of available coin denominations.

## Problem Description
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

### Function Prototype
```python
def makeChange(coins, total)
```

### Parameters
- `coins`: A list of the values of the coins in your possession (positive integers)
- `total`: The target amount to make change for

### Return Value
- Returns the fewest number of coins needed to meet the total
- Returns 0 if total is 0 or less
- Returns -1 if total cannot be met by any number of coins

## Algorithm
The solution uses dynamic programming with the following approach:

1. **Base Case**: If total ≤ 0, return 0
2. **Initialization**: Create a DP array where dp[i] represents the minimum coins needed for amount i
3. **Fill DP Array**: For each amount from 1 to total, try each coin denomination and update the minimum
4. **Result**: Return dp[total] if possible, otherwise -1

### Time Complexity
- **Time**: O(total × len(coins))
- **Space**: O(total)

## Example Usage
```python
makeChange([1, 2, 25], 37)  # Returns 7
makeChange([1256, 54, 48, 16, 102], 1453)  # Returns -1
```

## Files
- `0-making_change.py`: Main implementation
- `0-main.py`: Test file
- `README.md`: This documentation

## Requirements
- Ubuntu 20.04 LTS
- Python 3.4.3
- PEP 8 style compliance
- All files must be executable
- All files must end with a new line
- First line must be `#!/usr/bin/python3`