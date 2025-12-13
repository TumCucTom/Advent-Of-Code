import sys
import pyperclip as pc
from collections import deque

def copy_to_clipboard(result):
    """Prints the result and copies it to the clipboard."""
    print(result)
    pc.copy(result)

sys.setrecursionlimit(10**6)

# Directions mapping for movements: Up, Right, Down, Left
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def extract_integers_from_string(s):
    """Extracts all integers from a string."""
    return [int(x) for x in re.findall('-?\d+', s)]

# Reading the map and instructions from the input file
input_file = '../data/15.txt'
data = open(input_file).read().strip()

# Split the input into the map and movement instructions
warehouse_map, movement_instructions = data.split('\n\n')
warehouse_map = warehouse_map.split('\n')

def solve_warehouse(warehouse_map, instructions, double_map=False):
    """Solves the warehouse problem with robot movement and box pushing."""

    # Dimensions of the map
    rows = len(warehouse_map)
    cols = len(warehouse_map[0])

    # Convert the map to a list of lists for easier manipulation
    warehouse = [[warehouse_map[r][c] for c in range(cols)] for r in range(rows)]

    # Double the map if needed (part 2 logic)
    if double_map:
        expanded_warehouse = []
        for r in range(rows):
            expanded_row = []
            for c in range(cols):
                if warehouse[r][c] == '#':
                    expanded_row.append('#')
                    expanded_row.append('#')
                elif warehouse[r][c] == 'O':
                    expanded_row.append('[')
                    expanded_row.append(']')
                elif warehouse[r][c] == '.':
                    expanded_row.append('.')
                    expanded_row.append('.')
                elif warehouse[r][c] == '@':
                    expanded_row.append('@')
                    expanded_row.append('.')
            expanded_warehouse.append(expanded_row)
        warehouse = expanded_warehouse
        cols *= 2  # Since we doubled the map width

    # Find the initial position of the robot
    robot_row, robot_col = None, None
    for r in range(rows):
        for c in range(cols):
            if warehouse[r][c] == '@':
                robot_row, robot_col = r, c
                warehouse[r][c] = '.'  # Empty the starting position of the robot

    # Process the movement instructions
    for instruction in instructions:
        if instruction == '\n':
            continue

        # Get the direction of movement
        dr, dc = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}[instruction]

        # Calculate the next potential robot position
        next_row, next_col = robot_row + dr, robot_col + dc

        # Check if the robot can move to the next position
        if warehouse[next_row][next_col] == '#':
            continue  # Wall, cannot move

        elif warehouse[next_row][next_col] == '.':
            # Move the robot to the empty space
            robot_row, robot_col = next_row, next_col

        elif warehouse[next_row][next_col] in ['[', ']', 'O']:
            # If robot encounters a box or a box part, it tries to push it
            boxes_to_move = deque([(robot_row, robot_col)])
            visited = set()
            can_move = True

            # Explore the possible area to push the box
            while boxes_to_move:
                current_row, current_col = boxes_to_move.popleft()
                if (current_row, current_col) in visited:
                    continue
                visited.add((current_row, current_col))

                # Calculate the next position of the box
                next_box_row, next_box_col = current_row + dr, current_col + dc

                # Check if the robot can push the box
                if warehouse[next_box_row][next_box_col] == '#':
                    can_move = False
                    break  # Can't move into a wall

                if warehouse[next_box_row][next_box_col] in ['O', '[', ']']:
                    # Continue to explore the boxes or box parts
                    boxes_to_move.append((next_box_row, next_box_col))

                # Handle pushing box parts
                if warehouse[next_box_row][next_box_col] == '[':
                    boxes_to_move.append((next_box_row, next_box_col))
                    assert warehouse[next_box_row][next_box_col + 1] == ']'
                    boxes_to_move.append((next_box_row, next_box_col + 1))
                elif warehouse[next_box_row][next_box_col] == ']':
                    boxes_to_move.append((next_box_row, next_box_col))
                    assert warehouse[next_box_row][next_box_col - 1] == '['
                    boxes_to_move.append((next_box_row, next_box_col - 1))

            if not can_move:
                continue  # Skip this move, as the robot can't push the box

            # Move the boxes and robot
            while visited:
                for rr, cc in sorted(visited):
                    next_rr, next_cc = rr + dr, cc + dc
                    if (next_rr, next_cc) not in visited:
                        assert warehouse[next_rr][next_cc] == '.'
                        warehouse[next_rr][next_cc] = warehouse[rr][cc]
                        warehouse[rr][cc] = '.'
                        visited.remove((rr, cc))

            robot_row += dr
            robot_col += dc

    # Calculate the sum of the GPS coordinates of the boxes
    gps_sum = 0
    for r in range(rows):
        for c in range(cols):
            if warehouse[r][c] in ['[', 'O']:
                gps_sum += 100 * r + c

    return gps_sum

# Solve the warehouse puzzle (only the part related to pushing boxes)
result = solve_warehouse(warehouse_map, movement_instructions, double_map=True)

# Copy the result to clipboard and print it
copy_to_clipboard(result)
