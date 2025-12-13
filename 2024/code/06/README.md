# Solution Overview

The solution simulates the guard's movement based on a fixed set of rules and tests the effect of placing obstructions on the guard's path. It consists of two main parts:

### 1. Guard Movement Simulation
- The guard starts at a specified position and direction.
- The movement rules are:
    - If there’s an obstacle in front, the guard turns 90 degrees to the right.
    - Otherwise, the guard moves forward in the current direction.
- The simulation stops when the guard either revisits a state (position and direction) or leaves the grid.

### 2. Testing Obstructions
- The solution iterates over all empty spaces (`.`) in the grid and places an obstruction (`#`) in each position.
- For each obstruction, it reruns the guard's movement simulation.
- It counts the number of positions where placing an obstruction causes the guard to get stuck in a loop (i.e., revisiting the same position and direction).

### Functions Used:
- **`read_map(file_path)`**: Reads the grid from a file.
- **`get_guard_position_and_direction(grid)`**: Finds the guard's starting position and direction.
- **`turn_right(direction)`**: Determines the new direction after a 90-degree turn.
- **`simulate_guard_path(grid)`**: Simulates the guard's path and counts repeated states.
- **`test_obstructions(grid)`**: Tests the effect of placing obstructions on the guard's movement.

The code calculates:
- The total number of distinct positions visited by the guard.
- The number of valid positions where adding an obstruction would cause the guard to loop.
