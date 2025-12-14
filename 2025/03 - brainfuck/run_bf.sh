#!/bin/bash
# Run the Brainfuck solution
cd "$(dirname "$0")"

echo "Running Brainfuck interpreter..."
echo "Note: Current 1.bf is a skeleton - full implementation needed for complete solution"
echo ""

python3 bf_interpreter.py 1.bf < ../data/3.txt

echo ""
echo "Exit code: $?"
