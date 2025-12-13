import sys
import pyperclip as pc

# Function to print the result and also copy it to the clipboard
def print_and_copy(result):
    print(result)
    pc.copy(result)

# Increase the recursion limit to handle deep recursion in large grids
sys.setrecursionlimit(10**6)

# Input filename (default to '10.in' if no file is provided as argument)
input_file = "../data/10.txt"

# Initialize total_paths to store the result
total_paths = 0

# Reading the input grid and converting it to a 2D list of integers
input_data = open(input_file).read().strip()  # Read the entire input
grid = input_data.split('\n')  # Split by rows
grid = [[int(cell) for cell in row] for row in grid]  # Convert each character to an integer

# Get the number of rows (num_rows) and columns (num_columns) from the grid
num_rows = len(grid)
num_columns = len(grid[0])

# Dictionary to memoize the results of subproblems (to avoid redundant calculations)
memo = {}

# Function to calculate the number of ways to reach a 0 starting from (row, col)
def count_paths_to_zero(row, col):
    """Return number of ways to reach a 0 from the point (row, col)."""
    # Base case: If we're at a 0, there's exactly one way (we've reached our destination)
    if grid[row][col] == 0:
        return 1

    # If we've already computed this subproblem, return the stored result
    if (row, col) in memo:
        return memo[(row, col)]

    total = 0  # Initialize the count of ways

    # Explore the four possible directions (up, right, down, left)
    for delta_row, delta_col in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        next_row = row + delta_row  # Row after moving in the given direction
        next_col = col + delta_col  # Column after moving in the given direction

        # Ensure the new position is within the grid bounds and has the correct value
        # (it must be one less than the current value to continue the path)
        if 0 <= next_row < num_rows and 0 <= next_col < num_columns and grid[next_row][next_col] == grid[row][col] - 1:
            total += count_paths_to_zero(next_row, next_col)  # Add the paths from the new position

    # Store the result in memo to avoid recalculating
    memo[(row, col)] = total
    return total

# Iterate through the grid to find all starting points (where grid[row][col] == 9)
for row in range(num_rows):
    for col in range(num_columns):
        if grid[row][col] == 9:  # Starting point (value 9)
            total_paths += count_paths_to_zero(row, col)  # Add the paths from this starting point

# Print the total number of ways to reach 0 from all starting points
print_and_copy(total_paths)
