import sys
import re
from collections import deque
import pyperclip as pc

# Set recursion limit for deep searches
sys.setrecursionlimit(10**6)

# Directions for up, right, down, left movements
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Helper function to extract integers from a string
def extract_integers(s):
    return [int(x) for x in re.findall('-?\d+', s)]

# Function to print the result and copy it to the clipboard
def print_and_copy_to_clipboard(result):
    print(result)
    pc.copy(str(result))

# Load the map and initial conditions from input file
input_file = "../data/20.txt"
data = open(input_file).read().strip()

# Parse the map
grid = data.split('\n')
rows = len(grid)
cols = len(grid[0])
grid = [[grid[r][c] for c in range(cols)] for r in range(rows)]

# Find the start ('S') and end ('E') positions
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            start_row, start_col = r, c
        if grid[r][c] == 'E':
            end_row, end_col = r, c

# Store distances from the end ('E') to all other points
distances = {}
queue = deque([(0, end_row, end_col)])  # Initialize the queue with the end position
while queue:
    dist, row, col = queue.popleft()
    if (row, col) in distances:
        continue
    distances[(row, col)] = dist
    for dr, dc in DIRECTIONS:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != '#':
            queue.append((dist + 1, new_row, new_col))

# Function to find possible "cheat" positions based on movement and time limits
def find_possible_cheat_positions(initial_distance, cheat_time_limit):
    result = set()  # To store unique cheat path pairs
    queue = deque([(0, None, None, None, start_row, start_col)])  # Initialize queue with start position
    seen = set()  # To track visited states
    save_threshold = 100  # Save state threshold to avoid processing too many states

    while queue:
        distance, cheat_start, cheat_end, cheat_time, row, col = queue.popleft()
        assert cheat_end is None  # Assert no cheat end state at the start

        # Skip processing if the distance is too far
        if distance >= initial_distance - save_threshold:
            continue

        # If reached the end, process the cheat path
        if grid[row][col] == 'E':
            if cheat_end is None:
                cheat_end = (row, col)
            if distance <= initial_distance - save_threshold and (cheat_start, cheat_end) not in result:
                result.add((cheat_start, cheat_end))

        # Skip if the current state has already been visited
        if (row, col, cheat_start, cheat_end, cheat_time) in seen:
            continue
        seen.add((row, col, cheat_start, cheat_end, cheat_time))

        # If no cheat started, initiate a cheat start at the current position
        if cheat_start is None:
            assert grid[row][col] != '#'
            queue.append((distance, (row, col), None, cheat_time_limit, row, col))

        # Process the end of a cheat if time is not None
        if cheat_time is not None and grid[row][col] != '#':
            assert grid[row][col] in ['.', 'S', 'E']
            if distances[(row, col)] <= initial_distance - 100 - distance:
                result.add((cheat_start, (row, col)))

        # If the cheat time has finished, stop processing that cheat path
        if cheat_time == 0:
            continue
        else:
            # Explore all directions
            for dr, dc in DIRECTIONS:
                new_row, new_col = row + dr, col + dc
                if cheat_time is not None:
                    assert cheat_time > 0
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        queue.append((distance + 1, cheat_start, None, cheat_time - 1, new_row, new_col))
                else:
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != '#':
                        queue.append((distance + 1, cheat_start, cheat_end, cheat_time, new_row, new_col))

    return len(result)

# Calculate the initial distance from the start ('S') to the end ('E')
initial_distance = distances[(start_row, start_col)]

# Solve part two by finding the number of valid cheat paths with different time limits
result_part_two_1 = find_possible_cheat_positions(initial_distance, 2)
result_part_two_2 = find_possible_cheat_positions(initial_distance, 20)

# Print and copy the results to the clipboard
print_and_copy_to_clipboard(result_part_two_1)
print_and_copy_to_clipboard(result_part_two_2)
