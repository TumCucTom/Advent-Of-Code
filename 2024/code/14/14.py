import sys
import re
from collections import deque
import pyperclip as pc

# Function to print and copy the output to the clipboard
def pr(s):
    print(s)
    pc.copy(s)

sys.setrecursionlimit(10**6)  # Increase recursion limit for large grid sizes
DIRECTIONS = [(-1,0),(0,1),(1,0),(0,-1)]  # Directions for moving: up, right, down, left

# Helper function to extract integers from a string
def extract_integers(s):
    return [int(x) for x in re.findall(r'-?\d+', s)]


# Input file
input_file = "../data/14.txt"
GRID_WIDTH = 101  # Width of the grid (in tiles)
GRID_HEIGHT = 103  # Height of the grid (in tiles)

# List to store robot data: (position_x, position_y, velocity_x, velocity_y)
robots = []

# Read the input data and parse the robot's positions and velocities
data = open(input_file).read().strip()
for line in data.split('\n'):
    pos_x, pos_y, vel_x, vel_y = extract_integers(line)  # Extract position and velocity integers
    robots.append((pos_x, pos_y, vel_x, vel_y))  # Store in the robots list

# Start simulating robot movement over time
for time_step in range(1, 10**6):  # Iterate through each time step (up to 1 million steps)
    grid = [['.' for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]  # Initialize the grid with empty spaces ('.')

    # Move the robots and update their positions on the grid
    for i, (pos_x, pos_y, vel_x, vel_y) in enumerate(robots):
        pos_x += vel_x  # Update x position
        pos_y += vel_y  # Update y position
        pos_x %= GRID_WIDTH   # Wrap around the grid width (modulo GRID_WIDTH)
        pos_y %= GRID_HEIGHT   # Wrap around the grid height (modulo GRID_HEIGHT)
        robots[i] = (pos_x, pos_y, vel_x, vel_y)  # Update robot's position and velocity

        grid[pos_y][pos_x] = '#'  # Mark the robot's current position with '#'

    # Track the number of distinct robot components (connected groups of '#')
    component_count = 0
    visited_positions = set()  # Set to track already visited grid positions

    # BFS to explore and count connected components of robots ('#')
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if grid[y][x] == '#' and (x, y) not in visited_positions:  # Found a new component
                component_count += 1  # Increment the component count
                queue = deque([(x, y)])  # Initialize BFS queue with the current robot position
                while queue:
                    x2, y2 = queue.popleft()  # Pop the next position to explore
                    if (x2, y2) in visited_positions:
                        continue  # Skip if already visited
                    visited_positions.add((x2, y2))  # Mark the current position as visited
                    for dx, dy in DIRECTIONS:  # Explore neighbors (up, right, down, left)
                        xx, yy = x2 + dx, y2 + dy
                        if 0 <= xx < GRID_WIDTH and 0 <= yy < GRID_HEIGHT and grid[yy][xx] == '#':  # Valid robot position
                            queue.append((xx, yy))  # Add to queue for further exploration

    # Check if the number of components is less than or equal to 150
    if component_count <= 150:
        print(f"Time: {time_step}")  # Print the time when the condition is met

        # Generate the grid as a string for printing
        grid_str = [''.join(row) for row in grid]
        print('\n'.join(grid_str))  # Print the grid state
        break  # Exit the loop once the condition is satisfied
