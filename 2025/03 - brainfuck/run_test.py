#!/usr/bin/env python3
"""Test the BF interpreter and solve Day 3"""

def run_bf(code, input_data=''):
    """Execute Brainfuck code with given input."""
    tape = [0] * 30000
    ptr = 0
    input_ptr = 0
    
    # Find matching brackets
    bracket_map = {}
    stack = []
    for i, char in enumerate(code):
        if char == '[':
            stack.append(i)
        elif char == ']':
            start = stack.pop()
            bracket_map[start] = i
            bracket_map[i] = start
    
    pc = 0
    output = []
    
    while pc < len(code):
        char = code[pc]
        
        if char == '>':
            ptr += 1
        elif char == '<':
            ptr -= 1
        elif char == '+':
            tape[ptr] = (tape[ptr] + 1) % 256
        elif char == '-':
            tape[ptr] = (tape[ptr] - 1) % 256
        elif char == '.':
            output.append(chr(tape[ptr]))
        elif char == ',':
            if input_ptr < len(input_data):
                tape[ptr] = ord(input_data[input_ptr])
                input_ptr += 1
            else:
                tape[ptr] = 0
        elif char == '[':
            if tape[ptr] == 0:
                pc = bracket_map[pc]
        elif char == ']':
            if tape[ptr] != 0:
                pc = bracket_map[pc]
        
        pc += 1
    
    return ''.join(output)

# Test: Hello World
hello = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
result = run_bf(hello)
print(f"Hello World test: {repr(result)}")

# Now solve Day 3 using Python (the BF solution skeleton needs more work)
print("\n--- Day 3 Solution (Python verification) ---")

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

# Test examples
examples = ['987654321111111', '811111111111119', '234234234234278', '818181911112111']
for line in examples:
    print(f"  {line} -> {find_max_pair(line)}")
print(f"  Example sum: {sum(find_max_pair(l) for l in examples)} (expected: 357)")

# Solve actual puzzle
total = 0
with open('../data/3.txt') as f:
    for line in f:
        if line.strip():
            total += find_max_pair(line.strip())

print(f"\nPart 1 Answer: {total}")
