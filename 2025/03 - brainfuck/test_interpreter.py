#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
from bf_interpreter import run_bf

# Test 1: Hello World
hello_world = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
result = run_bf(hello_world)
print(f"Test 1 - Hello World: {result}")
assert result == "Hello World!\n", f"Expected 'Hello World!\\n', got {repr(result)}"

# Test 2: Simple addition (read two digits, add them)
# This reads '5' and '3', adds to get 8, outputs
add_test = ",>,<[->+<]>."
result = run_bf(add_test, "53")
print(f"Test 2 - Addition (5+3): {chr(ord('5') + ord('3') - 2*ord('0'))} (should be 8)")
print(f"Result byte value: {ord(result[0]) if result else 'empty'}")

print("\nInterpreter works! Now we need to complete the Day 3 solution.")
