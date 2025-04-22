# Pascal's Triangle

## Overview
This project implements Pascal's Triangle in Python. Pascal's Triangle is a triangular array of numbers where each number is the sum of the two directly above it. The edges of the triangle are always 1.

## Repository Structure
- **GitHub Repository**: `alx-interview`
- **Directory**: `0x00-pascal_triangle`
- **File**: `0-pascal_triangle.py` - Contains the implementation of the Pascal's Triangle function

## Function Description
The main function `pascal_triangle(n)` returns a list of lists of integers representing Pascal's Triangle of height `n`.

### Parameters
- `n` (int): Number of rows to generate

### Return Value
- If `n` ≤ 0: Returns an empty list
- Otherwise: Returns a list of lists where each inner list represents a row of Pascal's Triangle

### Example
```python
# Output for pascal_triangle(5):
[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
```

## Mathematical Properties of Pascal's Triangle
- Each number is the sum of the two numbers directly above it
- The first and last number in each row is always 1
- Each row `i` has `i+1` elements (0-indexed)
- The sum of values in row `n` is equal to 2^n
- The triangle is symmetric around its center

## Usage
```python
#!/usr/bin/python3
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """Print the triangle in a readable format"""
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

## Implementation Details
The implementation follows these steps:
1. Handle the edge case: If `n` ≤ 0, return an empty list
2. Initialize the triangle with the first row [1]
3. For each subsequent row:
   - Start with 1
   - Calculate middle elements by adding the two elements above
   - End with 1
   - Add the completed row to the triangle
4. Return the completed triangle

## Complexity Analysis
- **Time Complexity**: O(n²) where n is the number of rows
- **Space Complexity**: O(n²) to store all elements of the triangle

## Requirements
- Python 3.4 or later
- All files are executable
- All files should end with a new line
- The first line of all files should be `#!/usr/bin/python3`
- Code should follow PEP 8 style guidelines

## Author
ALX Software Engineering Program