import sys
from collections import deque
import pyperclip as pc

# Function to print the result and copy it to the clipboard
def pr(s):
    print(s)
    pc.copy(s)

# Set the recursion limit higher to handle deep recursions if necessary
sys.setrecursionlimit(10**6)

# Directions for moving up, right, down, and left (used for exploring neighbors)
DIRS = [(-1,0),(0,1),(1,0),(0,-1)]

# Input file, can be passed as a command-line argument or defaults to '12.in'
input_file = '../data/12.txt'

# Read and prepare the input grid (map of garden plots)
grid_input = open(input_file).read().strip()

# Split the input into rows
grid = grid_input.split('\n')

# Get the number of rows and columns in the grid
rows = len(grid)
cols = len(grid[0])

# Set to keep track of visited cells (to avoid counting the same region twice)
visited = set()

# Initialize total price for fencing (this will hold the final result)
total_price = 0

# Traverse each cell in the grid to explore regions of plants
for r in range(rows):
    for c in range(cols):
        if (r, c) in visited:
            continue  # Skip if the cell is already part of a previously visited region

        # Start BFS or DFS from this unvisited cell to find the entire region it belongs to
        queue = deque([(r, c)])  # Queue to hold cells to explore (for BFS)
        area = 0  # Variable to hold the area of the current region (number of garden plots in the region)
        perimeter = 0  # Variable to hold the perimeter of the current region (number of outer sides)
        perimeter_directions = dict()  # Dictionary to store the directions contributing to the perimeter for each region

        # Explore the region using BFS (breadth-first search)
        while queue:
            current_r, current_c = queue.popleft()  # Pop a cell from the queue for exploration

            if (current_r, current_c) in visited:
                continue  # Skip if the cell is already visited
            visited.add((current_r, current_c))  # Mark the cell as visited

            area += 1  # Increment the area of the region (each cell contributes one unit to the area)

            # Check the 4 adjacent cells (up, right, down, left)
            for dr, dc in DIRS:
                next_r, next_c = current_r + dr, current_c + dc

                # If adjacent cell is within bounds and has the same type of plant, continue exploring
                if 0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == grid[current_r][current_c]:
                    queue.append((next_r, next_c))  # Add the adjacent cell to the queue for further exploration
                else:
                    perimeter += 1  # If the adjacent cell is out of bounds or different, it contributes to the perimeter
                    if (dr, dc) not in perimeter_directions:
                        perimeter_directions[(dr, dc)] = set()  # Initialize a set to track perimeter directions
                    perimeter_directions[(dr, dc)].add((current_r, current_c))  # Store the current cell's position contributing to the perimeter

        # Count the number of unique sides (straight fence sections)
        sides = 0
        for direction, positions in perimeter_directions.items():
            visited_perimeter = set()  # Set to keep track of the perimeter cells we have already counted

            # For each direction, count the number of unique fence sides
            for pr, pc in positions:
                if (pr, pc) not in visited_perimeter:
                    sides += 1  # A new unique side is found
                    queue = deque([(pr, pc)])  # Start BFS to explore the perimeter section

                    # Explore the perimeter section to identify connected parts of the fence
                    while queue:
                        r2, c2 = queue.popleft()

                        if (r2, c2) in visited_perimeter:
                            continue  # Skip if this cell has already been processed
                        visited_perimeter.add((r2, c2))  # Mark this perimeter cell as visited

                        # Add adjacent perimeter parts to the queue for exploration
                        for dr, dc in DIRS:
                            rr, cc = r2 + dr, c2 + dc
                            if (rr, cc) in positions:
                                queue.append((rr, cc))  # Add the adjacent perimeter part to the queue

        # Calculate the price for this region: area * number of sides
        total_price += area * sides  # Add the cost of this region to the total price

# Print and copy the final total price to the clipboard
pr(total_price)
