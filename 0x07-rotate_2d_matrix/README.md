The solution implements the in-place 90-degree clockwise rotation using a two-step approach:
Algorithm Explanation:

Transpose the Matrix: Swap elements across the main diagonal (matrix[i][j] ↔ matrix[j][i])
Reverse Each Row: Reverse the order of elements in each row

How it works:
For the example matrix:
Original:     After Transpose:    After Row Reverse:
[1, 2, 3]  →  [1, 4, 7]       →  [7, 4, 1]
[4, 5, 6]     [2, 5, 8]          [8, 5, 2]
[7, 8, 9]     [3, 6, 9]          [9, 6, 3]
Key Features:

In-place operation: No additional matrix is created, only constant extra space is used
Time complexity: O(n²) - we visit each element once during transpose and once during row reversal
Space complexity: O(1) - only using constant extra space for swapping
No imports needed: Uses only built-in Python operations
Proper documentation: Includes docstring with example usage

The transpose operation only iterates through the upper triangle of the matrix (j > i) to avoid swapping elements twice, which would return them to their original positions.