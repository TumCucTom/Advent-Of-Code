import sys
import re
from collections import deque
import pyperclip as pc

# Increase recursion limit to handle large inputs
sys.setrecursionlimit(10**6)

# Directions for moving in the grid (up, right, down, left)
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left

def parse_integers_from_string(string):
    """
    Extracts all integers from a given string.
    """
    return [int(x) for x in re.findall('-?\d+', string)]

def print_and_copy_to_clipboard(result):
    """
    Prints the result to the console and copies it to the clipboard.
    """
    print(result)
    pc.copy(str(result))

# Input file path for the puzzle data
input_file_path = "../data/18.txt"

# Read the input data from the file and strip any extra whitespace
data = open(input_file_path).read().strip()

# Constants
GRID_SIZE = 71  # The grid is 71x71
grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Process the input and fill the grid with walls ('#') based on coordinates
for line in data.split('\n'):
    x, y = parse_integers_from_string(line)
    if 0 <= y < GRID_SIZE and 0 <= x < GRID_SIZE:
        grid[y][x] = '#'  # Mark the position as a wall

# Initialize a deque for BFS (breadth-first search)
queue = deque([(0, 0, 0)])  # Starting point (distance, row, column)
visited_positions = set()  # Set to track visited positions
goal_reached = False  # Flag to check if the goal is reached

# Perform BFS to find the shortest path from (0, 0) to (N-1, N-1)
while queue:
    distance, row, col = queue.popleft()

    # Check if we have reached the bottom-right corner (the goal)
    if (row, col) == (GRID_SIZE - 1, GRID_SIZE - 1):
        print_and_copy_to_clipboard(distance)  # Print and copy the result
        goal_reached = True
        break

    # Skip already visited positions
    if (row, col) in visited_positions:
        continue

    # Mark the current position as visited
    visited_positions.add((row, col))

    # Explore the neighboring cells
    for delta_row, delta_col in DIRECTIONS:
        new_row = row + delta_row
        new_col = col + delta_col

        # Ensure the new position is within bounds and is not a wall
        if 0 <= new_row < GRID_SIZE and 0 <= new_col < GRID_SIZE and grid[new_row][new_col] != '#':
            queue.append((distance + 1, new_row, new_col))  # Add the new position to the queue

# If the goal was not reached, print the position that failed
if not goal_reached:
    print_and_copy_to_clipboard(f"Goal not reached, last failed position: ({x},{y})")
