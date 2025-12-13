import sys
import z3
import re
import pyperclip as pc

# Function to print the result and copy it to clipboard
def pr(s):
    print(s)
    pc.copy(s)

# Increase recursion limit for large inputs
sys.setrecursionlimit(10**6)

# Directions for navigating the grid (up, right, down, left)
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Helper function to extract integers from a string
def ints(s):
    return [int(x) for x in re.findall('\d+', s)]

# Input file path
infile = "../data/13.txt"

# Initialize counter for total tokens spent
total_tokens = 0

# Read the input file content
input_data = open(infile).read().strip()

# Function to solve the claw machine problem
def solve_button_presses(ax, ay, bx, by, prize_x, prize_y):
    # Add a large offset to the prize location to ensure valid integer solutions
    prize_offset = 10000000000000
    prize_x += prize_offset
    prize_y += prize_offset

    # Define the number of presses for buttons A and B (t1 for A presses, t2 for B presses)
    t1 = z3.Int('t1')
    t2 = z3.Int('t2')

    # Set up the solver
    solver = z3.Solver()

    # Add constraints: t1 and t2 must be positive integers
    solver.add(t1 > 0)
    solver.add(t2 > 0)

    # The button presses must result in the target prize position
    solver.add(t1 * ax + t2 * bx == prize_x)  # X-axis constraint
    solver.add(t1 * ay + t2 * by == prize_y)  # Y-axis constraint

    # Solve the system of equations
    if solver.check() == z3.sat:
        model = solver.model()  # Get the solution model
        total_tokens = model.eval(3 * t1 + t2).as_long()  # Calculate the total cost (3 tokens for A, 1 token for B)
        return total_tokens
    else:
        # If no solution is found, return 0 tokens (impossible case)
        return 0

# Split input into individual machines
machines = input_data.split('\n\n')

# Loop through each machine's data and solve the problem
for machine in machines:
    ax, ay, bx, by, px, py = ints(machine)  # Parse the button presses and prize locations
    total_tokens += solve_button_presses(ax, ay, bx, by, px, py)

# Print and copy the result to clipboard
pr(total_tokens)
