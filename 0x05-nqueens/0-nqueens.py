#!/usr/bin/python3
"""
N Queens Problem Solver

This module solves the N Queens puzzle using backtracking algorithm.
The N Queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard.
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col].
    
    Args:
        board: Current state of the board
        row: Row position to check
        col: Column position to check
        n: Size of the board
    
    Returns:
        bool: True if safe to place queen, False otherwise
    """
    # Check this column on upper rows
    for i in range(row):
        if board[i] == col:
            return False
    
    # Check upper diagonal on left side
    for i in range(row):
        if board[i] == col - (row - i):
            return False
    
    # Check upper diagonal on right side
    for i in range(row):
        if board[i] == col + (row - i):
            return False
    
    return True


def solve_nqueens(board, row, n, solutions):
    """
    Solve N Queens problem using backtracking.
    
    Args:
        board: Current state of the board (list of column positions)
        row: Current row being processed
        n: Size of the board
        solutions: List to store all valid solutions
    """
    # Base case: If all queens are placed
    if row == n:
        # Convert board representation to required format
        solution = []
        for i in range(n):
            solution.append([i, board[i]])
        solutions.append(solution)
        return
    
    # Try placing queen in each column of current row
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place queen
            board[row] = col
            
            # Recursively place queens in remaining rows
            solve_nqueens(board, row + 1, n, solutions)
            
            # Backtrack (no need to explicitly remove queen
            # since we'll overwrite board[row] in next iteration)


def nqueens(n):
    """
    Main function to solve N Queens problem and print all solutions.
    
    Args:
        n: Size of the chessboard (n x n)
    """
    # Initialize board - board[i] represents column position of queen in row i
    board = [-1] * n
    solutions = []
    
    # Solve the problem
    solve_nqueens(board, 0, n, solutions)
    
    # Print all solutions
    for solution in solutions:
        print(solution)


def main():
    """
    Main function to handle command line arguments and input validation.
    """
    # Check number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    # Validate that N is an integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Solve N Queens problem
    nqueens(n)


if __name__ == "__main__":
    main()