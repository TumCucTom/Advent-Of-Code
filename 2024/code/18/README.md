# Solution Explanation for "Day 18: RAM Run"

This Python code solves the Advent of Code 2024 Day 18 problem, where you need to navigate a memory grid that is progressively corrupted by falling bytes. The goal is to find the shortest path to the exit while avoiding corrupted cells.

## Code Breakdown

### 1. **Imports and Setup**
The code uses several libraries:
- `sys` to set recursion limits for large inputs.
- `re` for parsing integers from input strings.
- `deque` for efficient BFS queue handling.
- `pyperclip` to copy the result to the clipboard.

### 2. **Grid Initialization**
The memory grid is represented as a 71x71 grid (71 rows and 71 columns). Initially, all cells are marked as safe (`.`), and falling bytes will convert cells to corrupted (`#`).

### 3. **Input Parsing**
The puzzle input contains the coordinates of falling bytes. These are parsed using the `parse_integers_from_string` function and used to mark the corresponding positions on the grid as corrupted.

### 4. **Breadth-First Search (BFS)**
The main algorithm uses BFS to find the shortest path from the top-left corner (0, 0) to the bottom-right corner (70, 70) while avoiding corrupted cells. The algorithm explores each cell's neighbors and processes them as long as they are safe and within bounds.

- The BFS starts at the top-left corner and checks each neighboring cell (up, down, left, right).
- It uses a queue to store the current position along with the distance from the start. Each visited cell is marked to avoid revisiting.
- If BFS reaches the exit, the distance is printed and copied to the clipboard.

### Conclusion
This code simulates the falling bytes, updates the grid, and uses BFS to efficiently find the shortest path to the exit while avoiding corrupted areas. It solves both parts of the problem by calculating the minimum number of steps required to reach the exit and identifying the first byte that blocks the path.
