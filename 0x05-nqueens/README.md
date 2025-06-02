# 0x05. N Queens

## Description

The N Queens puzzle is a classic problem in computer science that involves placing N non-attacking queens on an N×N chessboard. This project implements a solution using the backtracking algorithm.

## Problem Statement

Given an N×N chessboard, place N queens such that no two queens attack each other. Queens can attack horizontally, vertically, and diagonally.

## Algorithm

The solution uses **backtracking**, which is a systematic way of trying all possibilities:

1. **Place queens one by one** in different rows starting from the first row
2. **For each row**, try placing the queen in each column
3. **Check if placement is safe** (no conflicts with previously placed queens)
4. **If safe**, place the queen and recursively solve for the next row
5. **If not safe or no solution found**, backtrack and try the next column
6. **Repeat** until all solutions are found

## Key Concepts

### Backtracking
- Explores all potential solutions systematically
- Abandons solutions as soon as it's determined they cannot lead to a valid solution
- Backtracks to try alternative paths

### Safety Check
A position is safe if no previously placed queen can attack it:
- **Column conflict**: No queen in the same column
- **Diagonal conflict**: No queen on the same diagonal (both directions)

### Data Structure
- Uses a 1D array where `board[i]` represents the column position of the queen in row `i`
- This representation automatically handles row conflicts (one queen per row)

## Usage

```bash
./0-nqueens.py N
```

Where N is an integer ≥ 4.

### Examples

```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## Output Format

Each solution is printed as a list of `[row, column]` coordinates where each queen is placed.

## Error Handling

- **Wrong number of arguments**: "Usage: nqueens N"
- **N is not an integer**: "N must be a number"
- **N < 4**: "N must be at least 4"

## Time Complexity

- **Worst case**: O(N!) - exploring all possible arrangements
- **Average case**: Much better due to early pruning through backtracking

## Space Complexity

- O(N) for the board representation and recursion stack

## Files

- `0-nqueens.py`: Main implementation file
- `README.md`: This documentation file

## Requirements

- Python 3.4.3+
- Ubuntu 20.04 LTS
- PEP 8 compliant code
- Only `sys` module allowed for imports