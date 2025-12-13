# Boolean Circuit Solver

## Problem Overview

The problem involves:
1. Parsing a circuit description that includes initial wire values and gate instructions.
2. Simulating the circuit to compute output values for wires.
3. Combining the values of wires starting with `z` to form a binary number.
4. Converting the binary number to a decimal value.
5. Identifying and fixing errors in the circuit configuration.

## Code Explanation

### Input Parsing (`parse_input`)

The input file is split into two sections:
- **Wire Values Section:** Specifies the initial values for wires, such as `x00: 1`, `y01: 0`, etc.
- **Gate Instructions Section:** Lists boolean logic gates and their connections (e.g., `x00 AND y00 -> z00`).

The `parse_input_changed` function is used for testing. It sets a single wire (either `x` or `y`) to `1` based on the `change_index` provided, resetting all others to `0`.

### Simulating Gates (`simulate_gates`)

This function evaluates the logic gates in the circuit:
- It uses a queue to process gates in order of dependency.
- For each gate, it checks if its input wires have resolved values. If so, it computes the gate's output using the logic:
    - **AND:** Outputs `1` if both inputs are `1`.
    - **OR:** Outputs `1` if at least one input is `1`.
    - **XOR:** Outputs `1` if inputs are different.
- Gates whose inputs are not yet resolved are re-queued until all are processed.

### Computing Output (`compute_output`)

After simulating the gates:
- The wires starting with `z` are collected and treated as bits of a binary number.
- The binary number is constructed from these wires, ordered by bit significance.
- The binary number is converted to a decimal value and copied to the clipboard using the `pyperclip` library.

### Main Execution

1. The circuit is parsed and simulated to produce an initial result.
2. Wires causing incorrect behavior are identified using `test_wrong`.
3. Problematic gates are located using `find_swapped_gates`.
4. The final result is printed and copied to the clipboard.

## Part 1

1. **Accurate Simulation:** The code evaluates boolean logic gates and resolves wire dependencies correctly.
2. **Binary to Decimal Conversion:** The outputs of wires starting with `z` are combined into a binary number, which is converted to a decimal value.
3. **Error Diagnosis:** Incorrect wires and gates are identified by systematically modifying the circuit and testing outputs.
4. **Error Resolution:** The code identifies and fixes gate swaps to ensure the correct output is produced.

The final result is printed and copied to the clipboard for convenience.

## Part 2
Eventually, using code to find the 8 incorrect paths and knowing we were creating adders: I found the gates by hand with :
- every OR gate needs to be connected to 2 AND gates
- every AND gate that was not connected to an input must to an OR gate