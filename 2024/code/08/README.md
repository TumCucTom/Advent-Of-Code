# Solution Explanation: Resonant Collinearity Problem

This solution calculates the number of unique locations on a grid that contain an antinode, which is defined by the interaction of antennas emitting signals at the same frequency. The task is to find these locations based on two models: one for part one and one for part two of the problem.

## Code Breakdown

The solution consists of two main functions:

1. **`parse_map`**:
   This function reads the input map from a file, parsing the grid and identifying antenna locations. Each antenna is represented by a frequency (a letter or digit), and its position is stored along with the frequency. The function returns two things:
    - A `grid` representing the layout of the map.
    - A list of `antennas`, where each antenna is represented by its `(x, y)` position and its frequency.

2. **`calculate_antinodes`**:
   This function calculates all the unique antinode positions based on the list of antennas:
    - **Frequency Grouping**: Antennas are grouped by their frequency (e.g., `a`, `A`, `0`, etc.).
    - **Collinearity Check**: For each group, the function checks every possible pair of antennas to see if they lie on a straight line (i.e., they are collinear). If they are, the function calculates the positions of potential antinodes along the line extended in both directions.
    - **Valid Antinode Check**: Only positions within the grid are considered valid antinodes.

The function returns a set of all unique antinode positions.

## Part One Model

For part one, the task is to calculate antinodes that appear only when antennas are at twice the distance from each other. The solution ensures that the calculated antinodes fall within the boundaries of the grid.

## Part Two Model

In part two, the model is updated to consider all positions directly in line with any two antennas of the same frequency, regardless of distance. This results in a larger set of antinodes, including those that coincide with antenna positions themselves. The total number of unique antinodes is recalculated accordingly.


