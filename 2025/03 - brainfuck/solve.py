#!/usr/bin/env python3
"""Solve Day 3 and write answer to file"""

def find_max_pair(line):
    digits = [int(c) for c in line.strip() if c.isdigit()]
    if len(digits) < 2:
        return 0
    max_val = 0
    for i in range(len(digits) - 1):
        max_after = max(digits[i + 1:])
        val = digits[i] * 10 + max_after
        max_val = max(max_val, val)
    return max_val

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, '..', 'data', '3.txt')
output_path = os.path.join(script_dir, 'answer.txt')

# Test examples
examples = ['987654321111111', '811111111111119', '234234234234278', '818181911112111']
results = []
for line in examples:
    results.append(f"{line} -> {find_max_pair(line)}")
example_sum = sum(find_max_pair(l) for l in examples)
results.append(f"Example sum: {example_sum} (expected: 357)")

# Solve actual puzzle
total = 0
with open(data_path) as f:
    for line in f:
        if line.strip():
            total += find_max_pair(line.strip())

results.append(f"Part 1 Answer: {total}")

# Write to file
with open(output_path, 'w') as f:
    f.write('\n'.join(results))

# Also print
for r in results:
    print(r)
