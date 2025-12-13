# Reindeer Maze Solution

This solution addresses the problem of navigating a robot through a maze with obstacles, where the robot needs to reach a goal tile while optimizing its path in terms of both forward movement and rotation.

## Problem Breakdown

### Part 1: Finding the Shortest Path
- The robot starts at a designated "Start" tile ('S') and must reach the "End" tile ('E') in a maze.
- The robot can move one tile at a time (increasing its score by 1 point), or it can rotate 90 degrees (clockwise or counterclockwise) which increases its score by 1000 points.
- The goal is to find the shortest path from 'S' to 'E', considering both types of movement: forward and rotation.
- The solution uses **Dijkstra's Algorithm** with a priority queue to explore all possible movements and rotations efficiently.

### Part 2: Finding Optimal Positions
- After finding the shortest path from 'S' to 'E', we now explore the maze backwards from the "End" tile.
- The goal is to identify tiles that are part of any of the optimal paths. These tiles could be part of multiple best paths.
- We compute the number of such tiles, including 'S' and 'E', by checking whether their sum of distances from the start and the end equals the shortest path length.

## Code Explanation

### Key Functions:
1. **`output_result(result)`**: Prints the result and copies it to the clipboard.
2. **`parse_integers(input_string)`**: Converts a space-separated string of integers into a list of integers.
3. **Main Logic**: The algorithm works by using a priority queue to explore each tile in the maze, both in the forward direction (from 'S') and backward direction (from 'E'). The distances for each tile, considering different directions, are tracked to find the shortest path and optimal positions.

### Algorithm Details:
1. **Initialization**:
    - The maze is read from a text file, and the start ('S') and end ('E') positions are identified.
    - A 2D grid is created to represent the maze, and a priority queue is used to explore the grid.

2. **Exploration (Part 1)**:
    - We start from the 'S' position and explore all possible moves (forward and rotations) while keeping track of the shortest distance to each tile.
    - For each valid move (a move to an empty space or the end tile), the distance is updated and pushed into the priority queue.

3. **Exploration (Part 2)**:
    - The exploration is then done from the 'E' position in reverse, again using the same principle of tracking the shortest distance.
    - This allows us to compute the tiles that lie on the optimal paths by comparing distances from both directions.

4. **Output**:
    - The final output is the number of tiles that are part of the optimal paths through the maze.

### Example Walkthrough:
For the given example, after computing the shortest path and performing the backward exploration, the solution identifies that there are **45** tiles that are part of the best paths in the first case, and **64** tiles in the second case.

## Conclusion
The solution uses a combination of **Dijkstra's Algorithm** and efficient grid exploration with priority queues to compute both the shortest path and identify the optimal tiles in the maze. The program correctly calculates the number of optimal tiles for each part of the problem.
