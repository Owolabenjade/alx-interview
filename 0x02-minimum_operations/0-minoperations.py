#!/usr/bin/python3
"""
Module for calculating minimum operations to achieve n characters
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n 'H'
    characters in a file.
    
    Args:
        n (int): Target number of 'H' characters
        
    Returns:
        int: Minimum number of operations, or 0 if impossible
    """
    # If n is 1, we already have 'H' so no operations needed
    if n <= 1:
        return 0
    
    operations = 0
    i = 2
    
    # Continue until n is reduced to 1
    while i <= n:
        # If i is a factor of n
        if n % i == 0:
            # Divide n by i
            n = n // i
            # Add i to operations (Copy All + i-1 Pastes)
            operations += i
        else:
            # If i is not a factor, try the next number
            i += 1
    
    return operations