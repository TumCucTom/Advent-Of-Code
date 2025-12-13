# Advent of Code - Claw Contraption

## Problem Summary
The task is to solve the claw machine problem where each machine has two buttons (A and B) that move the claw by specific amounts in the X and Y axes. The goal is to determine the fewest tokens required to win as many prizes as possible, where each prize has a specific target position. Button A costs 3 tokens, and button B costs 1 token. The challenge is to find the optimal number of button presses for each machine.

## Solution Explanation

### Key Steps:
1. **Input Parsing**: The input consists of data for multiple claw machines. For each machine, the values for button A (X, Y movement) and button B (X, Y movement) are provided, along with the target prize location.

2. **Solving the Problem**:
    - For each machine, the code formulates the problem as a system of linear equations:
        - `t1 * ax + t2 * bx = prize_x` (for X-axis)
        - `t1 * ay + t2 * by = prize_y` (for Y-axis)
        - Where `t1` represents the number of presses for button A, and `t2` represents the number of presses for button B.
    - The constraints are that both `t1` and `t2` must be positive integers.

3. **Optimization**:
    - Using the `z3` library, a constraint solver is used to solve the system of equations and determine the values for `t1` and `t2` that satisfy both equations.
    - The total cost in tokens is calculated as `3 * t1 + t2`, where each press of button A costs 3 tokens and each press of button B costs 1 token.

4. **Handling Special Case (Part 2)**:
    - In part 2 of the puzzle, the target prize positions are offset by a large number (`10^13`) to make the positions large and non-trivial. The solver still handles this by adjusting the prize coordinates.

5. **Final Output**:
    - For each machine, the code checks if a valid solution exists (i.e., if there is a valid number of button presses that will land the claw on the prize).
    - If a valid solution is found, the number of tokens is added to the total count. If no solution is found, the machine is skipped.

6. **Result**: The total number of tokens required to win the maximum number of prizes is printed and copied to the clipboard.

### Code Overview:
- The `z3` solver is used to handle the system of equations efficiently.
- The input is read from a file, and the results are computed iteratively for each machine.
- The helper function `solve_button_presses` implements the logic to solve the linear equations and calculate the token cost.

