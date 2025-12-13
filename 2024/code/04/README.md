### Solution Overview

The code solves the Advent of Code puzzle by detecting X-MAS patterns in a grid. Here's how it works:

1. **Grid Processing:**
    - The grid is read from a file and converted into a 2D list of characters.

2. **Pattern Matching:**
    - For each cell, if the character is `'A'`, the code checks the surrounding diagonals for the "XMAS" pattern.
    - The pattern requires two diagonals to have "M" on one side and "S" on the opposite, forming an "X" with "MAS" components.

3. **Helper Functions:**
    - `check_diags` checks the four diagonals for valid "MAS" components.
    - `matches_pattern` verifies if a valid X-MAS pattern exists at a given position.
    - `count_xmas_patterns` iterates over the grid, counts all valid X-MAS patterns, and returns the result.

4. **Final Count:**
    - The total number of X-MAS patterns found in the grid is printed.

The code efficiently scans the grid and identifies all occurrences of the pattern based on diagonal relationships, handling edge cases as needed.
