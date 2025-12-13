# Merry Xmas!

# Solving the Lock and Key Compatibility Problem

## Problem Description
The task is to determine how many unique lock/key pairs are compatible based on given schematics. Each lock and key schematic is represented as a grid, and compatibility is defined by column heights that do not overlap beyond the available space.

## Steps to Solve

1. **Input Parsing**:
    - The input file is split into schematics separated by empty lines.
    - Locks are identified by having their top row filled (`#####`), and keys by their bottom row filled.

2. **Height Calculation**:
    - For locks:
        - Measure pin heights downward from the top `#` in each column until the first `.` is encountered.
    - For keys:
        - Measure key heights upward from the bottom `#` in each column until the first `.` is encountered.

3. **Compatibility Check**:
    - For each lock and key pair, check all columns to ensure that the sum of their respective heights does not exceed the total column height (number of rows in the schematic).

4. **Result Calculation**:
    - Iterate through all combinations of locks and keys.
    - Count pairs that meet the compatibility condition.

## Code Implementation
The solution involves:
- Reading and parsing the input.
- Converting schematics to numerical heights.
- Performing compatibility checks for all lock/key combinations.
- Outputting the result and copying it to the clipboard for convenience.
