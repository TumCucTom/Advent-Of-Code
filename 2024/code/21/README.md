# Advent of Code - Keypad Conundrum Solution

## Problem Overview
The task is to find the shortest sequence of button presses required to type codes on a keypad using a robot controlled by directional movements. The robot moves on a grid (keypad) with constraints on its allowed movements.

## Keypad Layout

### Pad 1:
```angular2html
+---+---+---+ | 7 | 8 | 9 | +---+---+---+ | 4 | 5 | 6 | +---+---+---+ | 1 | 2 | 3 | +---+---+---+ | 0 | A | +---+---+
```
### Pad 2:
```angular2html
+---+---+
| ^ | A |
+---+---+---+ | < | v | > | +---+---+---+
```


## Approach
The robot can move using a series of directional keypad commands (`<`, `>`, `^`, `v`). The solution leverages a breadth-first search (BFS) algorithm to explore the keypad and find the shortest sequence of button presses to type each code.

### Key Functions:
1. **`getPad1` & `getPad2`**: Return the button value at the current position on Pad1 and Pad2, respectively.
2. **`applyPad1` & `applyPad2`**: Update the robot's position on the keypads according to the movement direction.
3. **`solvePartTwo`**: Main BFS function that computes the shortest path to type the target code.

### BFS Search:
The BFS explores all possible moves the robot can make from its current position. The queue stores the robot's current state, and `seen` ensures no redundant calculations. The robot moves according to the allowed keypad directions and stops when it has typed the full code.

## Part One vs Part Two:
- **Part One**: Finds the shortest path to type each code on a keypad with fewer robots and simpler constraints.
- **Part Two**: Extends the problem with 25 robots, making the problem more complex but using the same BFS approach.

## Complexity:
The solution's complexity is determined by the length of the shortest sequence of moves required to type the code. Each code's complexity is calculated based on the numeric keypad layout and constraints.

## Final Notes:
This BFS-based solution efficiently computes the shortest sequence of button presses to type each code while respecting the constraints of the keypad's layout and movement restrictions.
