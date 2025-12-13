def read_map(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]

def get_guard_position_and_direction(grid):
    directions = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in directions:
                return (x, y), directions[cell]

    raise ValueError("Guard not found on the map")

def turn_right(direction):
    return {
        (0, -1): (1, 0),  # Up to Right
        (1, 0): (0, 1),   # Right to Down
        (0, 1): (-1, 0),  # Down to Left
        (-1, 0): (0, -1), # Left to Up
    }[direction]

def is_within_bounds(position, grid):
    x, y = position
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def simulate_guard_path(grid):
    position, direction = get_guard_position_and_direction(grid)

    visited = set()
    visited.add((position, direction))  # Save position and direction as a tuple
    run_count = 0  # Counter to track how many runs occur

    while is_within_bounds(position, grid):
        next_position = (position[0] + direction[0], position[1] + direction[1])

        if is_within_bounds(next_position, grid) and grid[next_position[1]][next_position[0]] != '#':
            position = next_position
        else:
            direction = turn_right(direction)

        state = (position, direction)  # Save position and direction as a tuple

        if state in visited:
            run_count += 1  # Increment the run counter if the state repeats
            break  # Exit the current simulation run due to a repeat
        visited.add(state)

        # Check if the guard goes off the grid, if so, stop the simulation
        if not is_within_bounds((position[0] + direction[0], position[1] + direction[1]), grid):
            break

    return run_count

def test_obstructions(grid):
    empty_spaces = [
        (x, y)
        for y, row in enumerate(grid)
        for x, cell in enumerate(row)
        if cell == '.'
    ]

    total_runs = 0  # Total number of runs with repeated states

    for x, y in empty_spaces:
        # Place an obstruction
        grid[y][x] = '#'

        # Run the simulation
        result = simulate_guard_path(grid)
        total_runs += result

        print(x,y)

        # Remove the obstruction
        grid[y][x] = '.'

    return total_runs

if __name__ == "__main__":
    file_path = "Data/6.txt"
    grid = read_map(file_path)

    # Test with obstructions
    total_repeated_runs = test_obstructions(grid)
    print("Total number of repeated states (run exits due to revisiting a state):", total_repeated_runs)
