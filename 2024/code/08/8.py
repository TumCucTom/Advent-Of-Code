def parse_map(file_path):
    """Parse the input map and extract antenna locations."""
    grid = []
    antennas = []
    with open(file_path, 'r') as file:
        for y, line in enumerate(file):
            grid.append(line.strip())
            for x, char in enumerate(line.strip()):
                if char != '.':
                    antennas.append((x, y, char))
    return grid, antennas

def calculate_antinodes(antennas):
    """Calculate all unique antinode positions."""
    antinodes = set()

    # Group antennas by frequency
    frequency_groups = {}
    for x, y, freq in antennas:
        frequency_groups.setdefault(freq, []).append((x, y))

    # Process each frequency group
    for freq, positions in frequency_groups.items():
        n = len(positions)
        for i in range(n):
            x1, y1 = positions[i]
            antinodes.add((x1, y1))  # Add the position of the antenna itself
            for j in range(i + 1, n):
                x2, y2 = positions[j]

                # Check if the antennas are collinear
                dx = x2 - x1
                dy = y2 - y1

                # Extend the line in both directions to find all antinodes
                for k in range(-100, 101):  # Large range to ensure coverage
                    ax = x1 + k * dx
                    ay = y1 + k * dy

                    # Add valid antinodes to the set
                    if 0 <= ax < len(grid[0]) and 0 <= ay < len(grid):
                        antinodes.add((ax, ay))

    return antinodes

# Load the map and calculate the result
file_path = '../data/8.txt'
grid, antennas = parse_map(file_path)
antinodes = calculate_antinodes(antennas)

# Print the total count of unique antinode positions
print("Total unique antinode locations:", len(antinodes))
