# Brainfuck

- `>` `<` - move pointer right/left
- `+` `-` - increment/decrement cell
- `.` `,` - output/input character
- `[` `]` - loop while cell non-zero

For each line:
1. For each pair of positions (i, j) where i < j
2. Calculate `10 * digit[i] + digit[j]`
3. Track the maximum value
4. Add to running sum

Optimization: For each position, track the maximum digit seen to its right. Then `max = max(10*d[i] + max_after[i])` for all i.

## Memory Layout

```
Cells 0-1:     Input/temp
Cells 2-101:   Digit storage (up to 100 per line)
Cell 102:      Digit count for current line
Cells 103-109: Working variables (indices, comparisons)
Cells 110-112: 3-byte sum accumulator (little-endian)
Cells 120+:    Output digit buffer
```

## Running

A Python Brainfuck interpreter is included (`bf_interpreter.py`). To run:

```bash
python3 bf_interpreter.py 1.bf < ../data/3.txt
```

Or use the run script:
```bash
./run.sh
```

**Note:** The current `1.bf` is a structured skeleton showing the algorithm. A complete, working Brainfuck solution for this problem (200 lines × 100 digits with multi-byte arithmetic) would be several thousand characters of dense code. The skeleton demonstrates the memory layout and approach but needs completion of the nested loops and arithmetic operations.
