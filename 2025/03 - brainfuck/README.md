# Brainfuck

8 commands only:
- `>` `<` - move pointer right/left
- `+` `-` - increment/decrement cell
- `.` `,` - output/input character
- `[` `]` - loop while cell non-zero

## Algorithm

For each line:
1. For each pair of positions (i, j) where i < j
2. Calculate `10 * digit[i] + digit[j]`
3. Track the maximum value
4. Add to running sum

Optimization: Track max digit to the right. Then `max = max(10*d[i] + max_after[i])`.

## Running

```bash
python3 bf_interpreter.py 1.bf < ../data/3.txt
```

Or verify with Python:
```bash
python3 run_all.py
```
