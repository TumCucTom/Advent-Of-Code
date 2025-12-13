# Warehouse Robot Problem Solution

This solution simulates the movements of a malfunctioning robot in a warehouse and computes the sum of the GPS coordinates of all the boxes after the robot has completed its moves. The problem consists of two parts, both related to simulating the robot's behavior in the warehouse.

## Problem Breakdown

### Input
The input consists of:
1. A grid map representing the warehouse.
2. A series of movement instructions for the robot.

Each tile in the grid can represent:
- `#` for a wall,
- `.` for an empty space,
- `O` for a box,
- `@` for the robot.

The movement instructions are a sequence of characters (`^`, `v`, `<`, `>`) that specify the direction in which the robot should attempt to move.

### Part 1: Simulating Robot and Box Movements
- The robot starts at a specified position (`@`) on the grid and moves according to the given instructions.
- If the robot encounters a box (`O`), it will attempt to push the box in the specified direction, provided there is no wall (`#`) blocking the path.
- The robot and boxes move in the grid, and if a box is pushed to an empty space (`.`), it occupies that space.
- After completing all moves, the sum of the GPS coordinates of the boxes is calculated. The GPS coordinate of a box is determined as `100 * row + column`.

### Part 2: Doubled Warehouse
- In this part, the map is doubled in width by applying the following transformations:
    - `#` becomes `##`
    - `O` becomes `[]`
    - `.` becomes `..`
    - `@` becomes `@.`
- The robot moves the boxes in the expanded warehouse, and boxes are now represented by two tiles (e.g., `[]` instead of `O`), which allows for pushing multiple boxes at once.
- The final sum of the GPS coordinates of the boxes is calculated similarly, with the new coordinates accounting for the expanded map.

## Code Explanation

### Key Functions:
1. **`copy_to_clipboard(result)`**: Prints the result and copies it to the clipboard.
2. **`extract_integers_from_string(s)`**: Extracts integers from a string using regular expressions.
3. **`solve_warehouse(warehouse_map, instructions, double_map=False)`**: This is the main function that:
    - Initializes the warehouse grid and robot position.
    - Handles the robot's movement and box-pushing logic.
    - Expands the warehouse if `double_map=True`.
    - Calculates and returns the sum of the GPS coordinates of all boxes after the robot finishes its moves.

### Algorithm Details:
1. **Movement Simulation**:
    - The robot follows the movement instructions, checking whether the destination is a wall or a box.
    - If it encounters a box, it attempts to push it to an adjacent empty space, provided there are no obstacles.
    - If the robot successfully pushes a box, it updates the grid and continues to the next instruction.

2. **GPS Calculation**:
    - After all movements are executed, the final grid state is used to compute the GPS coordinates of all boxes (`O` or `[]`), which are summed to produce the result.

### Example:
For the given input, the code simulates the robot's movements and calculates the sum of GPS coordinates based on the final grid configuration.

## Conclusion

This solution effectively simulates the robot’s behavior and box movements, both in a normal and expanded warehouse, to calculate the required GPS sum.

