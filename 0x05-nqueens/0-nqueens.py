#!/usr/bin/python3
"""
N Queens puzzle solver using backtracking algorithm.

The N Queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard. This program finds and prints all possible solutions.
"""

import sys


def is_safe(board, row, col):
    """
    Check if placing a queen at position (row, col) is safe.
    
    A position is safe if no other queen can attack it.
    Queens attack horizontally, vertically, and diagonally.
    
    Args:
        board (list): Current board state with queen positions
        row (int): Row to check
        col (int): Column to check
        
    Returns:
        bool: True if position is safe, False otherwise
    """
    # Check if any previously placed queen attacks this position
    for i in range(row):
        # Check column conflict
        if board[i] == col:
            return False
        
        # Check diagonal conflicts
        # Left diagonal: row difference equals column difference
        if abs(board[i] - col) == abs(i - row):
            return False
    
    return True


def solve_nqueens(n, row, board, solutions):
    """
    Recursively solve N Queens using backtracking.
    
    Args:
        n (int): Size of the chessboard (N×N)
        row (int): Current row being processed
        board (list): Current board state (board[i] = column of queen in row i)
        solutions (list): List to store all valid solutions
    """
    # Base case: if all queens are placed
    if row == n:
        # Convert board representation to required format
        solution = [[i, board[i]] for i in range(n)]
        solutions.append(solution)
        return
    
    # Try placing queen in each column of current row
    for col in range(n):
        if is_safe(board, row, col):
            # Place queen
            board[row] = col
            
            # Recursively place queens in remaining rows
            solve_nqueens(n, row + 1, board, solutions)
            
            # Backtrack (remove queen) - this happens automatically
            # when the function returns and board[row] gets overwritten


def nqueens(n):
    """
    Find and print all solutions to the N Queens problem.
    
    Args:
        n (int): Size of the chessboard
    """
    solutions = []
    board = [-1] * n  # board[i] represents column of queen in row i
    
    solve_nqueens(n, 0, board, solutions)
    
    # Print all solutions
    for solution in solutions:
        print(solution)


def main():
    """
    Main function to handle command line arguments and execute N Queens solver.
    """
    # Check number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    # Validate N is a number
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    # Validate N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Solve N Queens
    nqueens(n)


if __name__ == "__main__":
    main()