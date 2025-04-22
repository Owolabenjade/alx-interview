#!/usr/bin/python3
"""
Pascal's Triangle Module
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n.
    
    Args:
        n (int): Number of rows to generate
        
    Returns:
        list: Empty list if n <= 0, otherwise list of lists representing Pascal's triangle
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # Start with the first row
    
    for i in range(1, n):
        # Previous row
        prev_row = triangle[-1]
        
        # Start new row (always begins with 1)
        new_row = [1]
        
        # Calculate middle elements (sum of the two numbers above)
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])
        
        # Append the final 1 (every row ends with 1)
        new_row.append(1)
        
        # Add the new row to our triangle
        triangle.append(new_row)
    
    return triangle