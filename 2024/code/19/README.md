# Solution Explanation for "Day 19: Linen Layout"

This Python code solves the Advent of Code 2024 Day 19 problem, where you need to calculate how many ways different towel patterns can form desired designs based on available towel patterns.

## Code Breakdown

### 1. **Imports and Setup**
The code uses several libraries:
- `sys` to increase recursion limits for large input sizes.
- `z3` for potential future use (though not utilized in the current solution).
- `re` for extracting integers from strings.
- `heapq` for priority queue operations (not used here).
- `defaultdict`, `Counter`, and `deque` for handling collections (partly unused in this problem).
- `sympy.solvers.solveset.linsolve` is imported but not used.
- `pyperclip` to copy the results to the clipboard.

### 2. **Helper Functions**
- **`output_result(result)`**: Prints the result to the console and copies it to the clipboard.
- **`extract_integers(text)`**: Extracts integers from a string using regular expressions.

### 3. **Reading and Parsing Input**
The input is read from a file and split into two sections:
- The first section contains the available towel patterns.
- The second section contains the target designs the onsen wants to create.

Both sections are parsed into lists:
- `patterns`: List of available towel patterns.
- `target_strings`: List of target designs that need to be formed using the available towel patterns.

### 4. **Memoization for Efficient Calculation**
The algorithm uses **memoization** to cache previously calculated results for target strings. This reduces redundant calculations when trying to form target designs from patterns.

### 5. **Recursive Function to Calculate Ways to Form Targets**
The `calculate_ways_to_form_target` function recursively calculates how many ways a given target string can be formed using available patterns:
- If the target is empty, there’s exactly one way to form it (by not using any more patterns).
- For each pattern, it checks if it can be used at the start of the target string. If so, it reduces the target string by removing the matched pattern and calls the function again recursively to calculate the remaining ways to form the rest of the target.
- The result is cached in `memoization_cache` to avoid redundant calculations.

### 6. **Calculating Formable Targets and Total Ways**
The code then iterates over all target strings:
- It calculates how many ways each target string can be formed using the available towel patterns.
- If a target string can be formed at least once, it increments the `total_formable_targets`.
- It adds the number of ways to form each target string to the `total_ways_to_form_all_targets`.

### 7. **Output**
Finally, the results are printed and copied to the clipboard:
- `total_formable_targets`: The count of target designs that can be formed using the available patterns.
- `total_ways_to_form_all_targets`: The sum of all the different ways each target design can be formed.

### Conclusion
This code solves the problem by using dynamic programming with memoization to calculate how many ways each target string can be formed using a list of available towel patterns. It efficiently handles large input sizes and provides the correct number of formable targets and ways to form them.
