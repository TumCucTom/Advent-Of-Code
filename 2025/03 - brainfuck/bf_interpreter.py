#!/usr/bin/env python3
"""
Simple Brainfuck interpreter
"""
import sys

def run_bf(code, input_data=''):
    """Execute Brainfuck code with given input."""
    # Initialize tape (30,000 cells, 8-bit)
    tape = [0] * 30000
    ptr = 0
    input_ptr = 0
    
    # Preprocess: find matching brackets
    bracket_map = {}
    stack = []
    for i, char in enumerate(code):
        if char == '[':
            stack.append(i)
        elif char == ']':
            if not stack:
                raise ValueError(f"Unmatched ']' at position {i}")
            start = stack.pop()
            bracket_map[start] = i
            bracket_map[i] = start
    
    if stack:
        raise ValueError(f"Unmatched '[' at position {stack[-1]}")
    
    # Execute
    pc = 0  # program counter
    output = []
    
    while pc < len(code):
        char = code[pc]
        
        if char == '>':
            ptr += 1
            if ptr >= len(tape):
                tape.extend([0] * 1000)
        elif char == '<':
            ptr -= 1
            if ptr < 0:
                raise ValueError("Pointer moved below zero")
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
                tape[ptr] = 0  # EOF = 0
        elif char == '[':
            if tape[ptr] == 0:
                pc = bracket_map[pc]
        elif char == ']':
            if tape[ptr] != 0:
                pc = bracket_map[pc]
        
        pc += 1
    
    return ''.join(output)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 bf_interpreter.py <file.bf> [input]")
        sys.exit(1)
    
    with open(sys.argv[1], 'r') as f:
        code = f.read()
    
    # Filter out non-BF characters (comments)
    code = ''.join(c for c in code if c in '><+-.,[]')
    
    input_data = sys.stdin.read() if len(sys.argv) == 2 else sys.argv[2]
    
    try:
        output = run_bf(code, input_data)
        print(output, end='')
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
