# Solution Explanation: Hoof It Problem

This solution tackles the "Hoof It" problem by calculating the number of distinct hiking trails from each trailhead and determining the sum of trailhead scores or ratings based on the topographic map provided.

## Code Breakdown

1. **`print_and_copy(result)`**:
   This helper function prints the result and also copies it to the clipboard using the `pyperclip` module.

2. **Input Parsing**:
    - The input file is read, and the topographic map is processed into a 2D list of integers, representing the heights at each position on the grid.

3. **`count_paths_to_zero(row, col)`**:
   This function recursively calculates the number of ways to reach a height of 0 from a starting point on the grid (starting from any cell marked `9`).
    - **Base case**: If the current cell's height is 0, there’s exactly one way to reach the destination.
    - **Memoization**: To avoid recalculating the same subproblems, the function stores the results of previously computed paths in a `memo` dictionary.

4. **Main Calculation Loop**:
    - The grid is iterated to find all the starting points (cells with height `9`).
    - For each starting point, the function `count_paths_to_zero` is called to count how many paths from that point reach a `0`.
    - The total number of paths across all starting points is accumulated.

5. **Memoization for Efficiency**:
    - The memoization technique significantly reduces the time complexity by ensuring that each subproblem (a cell's path count) is calculated only once.

6. **Result Output**:
    - After all the paths are counted, the total number of distinct hiking trails is printed and copied to the clipboard.

## Problem Models

- **Part One (Trailhead Score)**:
  In this part, the goal is to calculate the number of hiking trails starting from each trailhead (height `0`) and ending at a height `9`. Each trailhead's score is the number of reachable `9`-height positions from it.

- **Part Two (Trailhead Rating)**:
  In this part, the goal is to compute the number of distinct hiking trails originating from each trailhead, which is equivalent to finding all unique paths that start at each trailhead and reach a height `9`.

