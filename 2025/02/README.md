# Advent of Code 2025 - Day 2: Gift Shop

SWI Prolog solutions for finding invalid product IDs.

## Problem

### Part 1
Find all product IDs in given ranges that are invalid. An invalid ID is one where the digits form a pattern repeated exactly twice (e.g., 55, 6464, 123123).

### Part 2
Find all product IDs that are invalid under new rules. An invalid ID is one where the digits form a pattern repeated at least twice (e.g., 12341234, 123123123, 1212121212, 1111111).

## Solutions

- `1.pl` - Part 1 solution (pattern repeated exactly twice)
- `2.pl` - Part 2 solution (pattern repeated at least twice)

## Running

```bash
# Run Part 1
swipl -q -t 'main, halt.' 1.pl

# Run Part 2
swipl -q -t 'main, halt.' 2.pl

# Test Part 2 with example
swipl -q -t 'test_example, halt.' 2.pl
```

## Algorithm

Both solutions:
1. Parse the input file to extract ID ranges
2. For each range, generate invalid numbers by creating patterns and repeating them
3. Filter to only include numbers within the range
4. Sum all invalid IDs

Part 2 checks for patterns repeated 2, 3, 4, ... times, while Part 1 only checks for exactly 2 repetitions.
