import sys
import pyperclip as pc
import re

# Setting recursion limit for deep recursions, to prevent hitting system limits
sys.setrecursionlimit(10**6)

# Function to print a result and copy it to the clipboard
def print_and_copy(result):
    print(result)
    pc.copy(str(result))

# Helper function to extract all integers from a string
def extract_integers(s):
    return [int(x) for x in re.findall('-?\d+', s)]

# Constants for the task
input_file = "../data/22.txt"

# Read the input data from the file
with open(input_file) as f:
    data = f.read().strip()

# Function to mix two integers using XOR operation
def mix_values(x, y):
    return x ^ y

# Function to prune an integer by taking modulo 16777216
def prune_value(x):
    return x % 16777216

# Function to simulate a series of operations on an initial value (x)
def generate_values(initial_value):
    # Starting with the initial value, we generate a sequence of 2000 values
    values = [initial_value]
    for _ in range(2000):
        initial_value = prune_value(mix_values(initial_value, 64 * initial_value))  # Mix and prune
        initial_value = prune_value(mix_values(initial_value, initial_value // 32))  # Mix and prune again
        initial_value = prune_value(mix_values(initial_value, initial_value * 2048))  # Mix and prune
        values.append(initial_value)  # Append the result to the sequence
    return values

# Function to calculate the changes between consecutive values in a list
def calculate_changes(values):
    return [values[i+1] - values[i] for i in range(len(values) - 1)]

# Function to map 4 consecutive changes to a score
def calculate_scores(values, changes):

    scores = {}
    # Iterate through the changes and map every 4 consecutive changes to the value that follows them
    for i in range(len(changes) - 3):
        pattern = (changes[i], changes[i+1], changes[i+2], changes[i+3])
        if pattern not in scores:
            scores[pattern] = values[i + 4]
    return scores

# Dictionary to store all the scores accumulated from patterns
accumulated_scores = {}

# Process each line in the input data
for line in data.split('\n'):
    # Convert the current line into a sequence of values
    initial_value = int(line)
    generated_values = generate_values(initial_value)

    # Prune the values by taking modulo 10 (to reduce size and for pattern recognition)
    pruned_values = [x % 10 for x in generated_values]

    # Calculate the differences (changes) between consecutive pruned values
    value_changes = calculate_changes(pruned_values)

    # Calculate the scores based on patterns in the changes
    scores = calculate_scores(pruned_values, value_changes)

    # Accumulate the scores for each pattern in the dictionary
    for pattern, score in scores.items():
        if pattern not in accumulated_scores:
            accumulated_scores[pattern] = score
        else:
            accumulated_scores[pattern] += score

# Output the maximum score found in the accumulated scores
max_score = max(accumulated_scores.values())

# Print and copy the result
print_and_copy(max_score)
