# 0x09. Island Perimeter

## Description
This project implements a function to calculate the perimeter of an island in a 2D grid.

## Algorithm
The solution iterates through each cell in the grid and for each land cell (1), checks its four neighbors. For each neighbor that is either water (0) or outside the grid boundary, we add 1 to the perimeter count.

## Files
- `0-island_perimeter.py`: Main solution file containing the `island_perimeter` function
- `0-main.py`: Test file to verify the solution

## Usage
```python
from 0-island_perimeter import island_perimeter

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
