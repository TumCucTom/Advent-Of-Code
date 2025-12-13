import sys
import re
import pyperclip as pc

# Function to print and copy output to the clipboard
def output_result(result):
    print(result)
    pc.copy(str(result))

# Increase recursion limit to handle larger depths in the recursion
sys.setrecursionlimit(10**6)

# Directional movements (up, right, down, left) - not used in this problem but added for reference
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Function to extract all integers from a string
def extract_integers(text):
    return [int(x) for x in re.findall('-?\d+', text)]

# Read and parse the input file
input_file = "../data/19.txt"
data = open(input_file).read().strip()
patterns_section, target_strings_section = data.split('\n\n')

# Split the patterns (words) and targets by commas and newlines
patterns = patterns_section.split(', ')
target_strings = target_strings_section.split('\n')

# Memoization dictionary to store previously computed results
memoization_cache = {}

# Recursive function to calculate how many ways the words can form the target string
def calculate_ways_to_form_target(patterns, target):
    if target in memoization_cache:
        return memoization_cache[target]

    # Base case: if the target string is empty, we found one way to form it (by not using any more words)
    ways_count = 0
    if not target:
        ways_count = 1

    # Try each pattern and see if it starts with the target string
    for pattern in patterns:
        if target.startswith(pattern):
            ways_count += calculate_ways_to_form_target(patterns, target[len(pattern):])

    # Store the result in the cache
    memoization_cache[target] = ways_count
    return ways_count

# Variables to store the count of targets that can be formed and the total number of ways to form all targets
total_formable_targets = 0
total_ways_to_form_all_targets = 0

# Process each target string
for target_string in target_strings:
    ways_to_form_target = calculate_ways_to_form_target(patterns, target_string)

    # If the target string can be formed, increment the count of formable targets
    if ways_to_form_target > 0:
        total_formable_targets += 1

    # Add the total number of ways this target can be formed to the cumulative total
    total_ways_to_form_all_targets += ways_to_form_target

# Output the results: number of formable targets and total ways to form all targets
output_result(total_formable_targets)
output_result(total_ways_to_form_all_targets)
