import sys
import heapq
import pyperclip as pc

# Function to print and copy result to clipboard
def output_result(result):
    print(result)
    pc.copy(str(result))

# Set the recursion limit for the program (in case of deep recursion)
sys.setrecursionlimit(10**6)

# Directions corresponding to up, right, down, and left movements
MOVEMENT_DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left

# Helper function to parse input string into integer list
def parse_integers(input_string):
    return [int(x) for x in input_string.split()]

# Read the input file containing the grid
input_file = "../data/16.txt"
data = open(input_file).read().strip()

# Initialize the grid from the input
grid = data.split('\n')
num_rows = len(grid)
num_columns = len(grid[0])

# Initialize the grid in a 2D list form
grid = [[grid[r][c] for c in range(num_columns)] for r in range(num_rows)]

# Find start (S) and end (E) positions
for row in range(num_rows):
    for col in range(num_columns):
        if grid[row][col] == 'S':
            start_row, start_col = row, col
        if grid[row][col] == 'E':
            end_row, end_col = row, col

# Priority queue to manage exploration, starting at the 'S' position
priority_queue = []
explored = set()  # Set to track already visited (row, column, direction)
heapq.heappush(priority_queue, (0, start_row, start_col, 1))  # (distance, row, col, direction)
distance_from_start = {}
shortest_path = None

# Part 1: Explore the grid in all directions from the start position
while priority_queue:
    distance, row, col, direction = heapq.heappop(priority_queue)

    # Record the distance from the start to (row, col) in the given direction
    if (row, col, direction) not in distance_from_start:
        distance_from_start[(row, col, direction)] = distance

    # Stop once we reach the end position and record the shortest path
    if row == end_row and col == end_col and shortest_path is None:
        shortest_path = distance

    # Skip if this position has been visited before in this direction
    if (row, col, direction) in explored:
        continue

    explored.add((row, col, direction))

    # Move in the current direction (e.g., up, right, down, or left)
    dr, dc = MOVEMENT_DIRECTIONS[direction]
    new_row, new_col = row + dr, col + dc

    # Only move to valid positions within the grid that aren't walls (#)
    if 0 <= new_col < num_columns and 0 <= new_row < num_rows and grid[new_row][new_col] != '#':
        heapq.heappush(priority_queue, (distance + 1, new_row, new_col, direction))

    # Try turning the robot (turn right, turn left)
    heapq.heappush(priority_queue, (distance + 1000, row, col, (direction + 1) % 4))  # Turn right
    heapq.heappush(priority_queue, (distance + 1000, row, col, (direction + 3) % 4))  # Turn left

#output_result(shortest_path)

# Part 2: Explore the grid backwards from the end position
priority_queue = []
explored = set()
for direction in range(4):
    heapq.heappush(priority_queue, (0, end_row, end_col, direction))  # Starting from the end position in all directions
distance_from_end = {}

# Explore the grid backwards from the end position
while priority_queue:
    distance, row, col, direction = heapq.heappop(priority_queue)

    # Record the distance from the end to (row, col) in the given direction
    if (row, col, direction) not in distance_from_end:
        distance_from_end[(row, col, direction)] = distance

    # Skip if this position has been visited before in this direction
    if (row, col, direction) in explored:
        continue

    explored.add((row, col, direction))

    # Move backwards (opposite direction)
    dr, dc = MOVEMENT_DIRECTIONS[(direction + 2) % 4]
    new_row, new_col = row + dr, col + dc

    # Only move to valid positions within the grid that aren't walls (#)
    if 0 <= new_col < num_columns and 0 <= new_row < num_rows and grid[new_row][new_col] != '#':
        heapq.heappush(priority_queue, (distance + 1, new_row, new_col, direction))

    # Try turning the robot (turn right, turn left) while going backwards
    heapq.heappush(priority_queue, (distance + 1000, row, col, (direction + 1) % 4))  # Turn right
    heapq.heappush(priority_queue, (distance + 1000, row, col, (direction + 3) % 4))  # Turn left

# Find positions that are on the optimal path by checking distances from both start and end
optimal_positions = set()
for row in range(num_rows):
    for col in range(num_columns):
        for direction in range(4):
            # A position is on an optimal path if the sum of distances from start to it and from it to end equals the shortest path
            if (row, col, direction) in distance_from_start and (row, col, direction) in distance_from_end:
                if distance_from_start[(row, col, direction)] + distance_from_end[(row, col, direction)] == shortest_path:
                    optimal_positions.add((row, col))

# Output the number of optimal positions
output_result(len(optimal_positions))
