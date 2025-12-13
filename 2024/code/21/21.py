import heapq
from collections import deque
import pyperclip as pc


# Pads Configuration
pad1 = ['789', '456', '123', ' 0A']
pad2 = [' ^A', '<v>']


# Helper function to get the value on Pad1 given coordinates
def getPad1(position):
    r, c = position
    if not (0 <= r < len(pad1) and 0 <= c < len(pad1[r])):
        return None
    if pad1[r][c] == ' ':
        return None
    return pad1[r][c]


# Helper function to get the value on Pad2 given coordinates
def getPad2(position):
    r, c = position
    if not (0 <= r < len(pad2) and 0 <= c < len(pad2[r])):
        return None
    if pad2[r][c] == ' ':
        return None
    return pad2[r][c]


# Helper function to apply a move on Pad1
def applyPad1(position, move):
    if move == 'A':
        return position, getPad1(position)
    elif move == '<':
        return (position[0], position[1] - 1), None
    elif move == '^':
        return (position[0] - 1, position[1]), None
    elif move == '>':
        return (position[0], position[1] + 1), None
    elif move == 'v':
        return (position[0] + 1, position[1]), None


# Helper function to apply a move on Pad2
def applyPad2(position, move):
    if move == 'A':
        return position, getPad2(position)
    elif move == '<':
        return (position[0], position[1] - 1), None
    elif move == '^':
        return (position[0] - 1, position[1]), None
    elif move == '>':
        return (position[0], position[1] + 1), None
    elif move == 'v':
        return (position[0] + 1, position[1]), None


# Function to solve part two of the problem, finding the shortest path
def solvePartTwo(target_code):
    # Start position and initial setup for the movement
    start = [0, (0, 2), '', '']
    queue = deque([start])
    seen = set()

    while queue:
        distance, position, output, path = queue.popleft()
        key = (position, output)

        # If the output matches the target code, return the path
        if output == target_code:
            pc.copy(path)  # Copy the result to clipboard
            return path

        # If the output is already too long, skip
        if not target_code.startswith(output):
            continue

        # Skip if this state has already been visited
        if key in seen:
            continue

        seen.add(key)

        # Ensure the position is valid
        if getPad2(position) is None:
            continue

        # Try all possible moves
        for move in ['^', '<', 'v', '>', 'A']:
            new_position = position
            new_output = output
            new_position, output_move = applyPad2(position, move)

            if output_move is not None:
                new_output = new_output + output_move

            # Append the new state to the queue
            queue.append([distance + 1, new_position, new_output, path + move])


# Main entry point for running the solution
if __name__ == "__main__":
    # Input target code to solve for
    target_code = "123"  # Example target code, change as needed

    # Solve part two with the given target code
    result = solvePartTwo(target_code)
    print(result)  # Output the solution

