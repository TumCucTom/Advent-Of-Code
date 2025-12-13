import pyperclip

def parse_input(file_path):
    with open(file_path, 'r') as f:
        sections = f.read().split("\n\n")

    # Parse wire values
    wire_values = {}
    for line in sections[0].splitlines():
        wire, value = line.split(": ")
        wire_values[wire] = int(value)

    # Parse gate instructions
    gates = []
    for line in sections[1].splitlines():
        parts = line.split(" ")
        input1, gate_type, input2, _, output = parts
        gates.append((input1, gate_type, input2, output))

    return wire_values, gates

def parse_input_changed(file_path, change_index):
    with open(file_path, 'r') as f:
        sections = f.read().split("\n\n")

    # Parse wire values
    wire_values = {}
    for line in sections[0].splitlines():
        wire, value = line.split(": ")
        wire_values[wire] = 0

    if change_index<45:
        wire_values[f'x{change_index:02}'] = 1
    else:
        change_index-=45
        wire_values[f'y{change_index:02}'] = 1

    # Parse gate instructions
    gates = []
    for line in sections[1].splitlines():
        parts = line.split(" ")
        input1, gate_type, input2, _, output = parts
        gates.append((input1, gate_type, input2, output))

    return wire_values, gates

def simulate_gates(wire_values, gates):
    # Use a queue to efficiently process gates
    from collections import deque

    gate_queue = deque(gates)
    resolved = set(wire_values.keys())

    while gate_queue:
        for _ in range(len(gate_queue)):
            input1, gate_type, input2, output = gate_queue.popleft()

            if input1 in resolved and input2 in resolved:
                # Get input values
                val1 = wire_values[input1]
                val2 = wire_values[input2]

                # Compute output based on gate type
                if gate_type == "AND":
                    wire_values[output] = val1 & val2
                elif gate_type == "OR":
                    wire_values[output] = val1 | val2
                elif gate_type == "XOR":
                    wire_values[output] = val1 ^ val2

                # Mark the output wire as resolved
                resolved.add(output)
            else:
                # Requeue the gate if inputs are not yet resolved
                gate_queue.append((input1, gate_type, input2, output))

    return wire_values

def find_connected_gates(start_wire, gates):
    # Find all gates that depend on the given start wire
    connected_gates = []
    to_check = [start_wire]

    # Iterate through the gates, collecting those that depend on the output of previous gates
    while to_check:
        current_wire = to_check.pop()
        for gate in gates:
            left_wire, right_wire = gate
            if left_wire == current_wire and right_wire not in to_check:
                to_check.append(right_wire)
                connected_gates.append(gate)

    return connected_gates

def compute_output(wire_values):
    # Collect all wires starting with 'z' and sort by bit significance
    z_wires = {k: v for k, v in wire_values.items() if k.startswith('z')}
    binary_number = ''.join(str(z_wires[f'z{i:02}']) for i in reversed(range(len(z_wires))))

    # Copy result to clipboard
    decimal_result = int(binary_number, 2)
    pyperclip.copy(str(decimal_result))

    # Convert binary to decimal
    return decimal_result

def test_wrong():
    bad = []
    for i in range(90):
        file_path = "../data/24.txt"
        wire_values, gates = parse_input_changed(file_path,i)
        wire_values = simulate_gates(wire_values, gates)
        result = compute_output(wire_values)

        if result != 2**(i%45):
            if i<45:
                bad.append(f'x{i:02}')
            else:
                bad.append(f'y{i-45:02}')

    print(bad)
    return bad

def get_expected_result(wire_values):
    x_wires = {k: v for k, v in wire_values.items() if k.startswith('x')}
    x_binary_number = ''.join(str(x_wires[f'z{i:02}']) for i in reversed(range(len(x_wires))))

    y_wires = {k: v for k, v in wire_values.items() if k.startswith('y')}
    y_binary_number = ''.join(str(x_wires[f'z{i:02}']) for i in reversed(range(len(y_wires))))

    # Copy result to clipboard
    x = int(x_binary_number, 2)
    y = int(y_binary_number,2)

    return x + y

def find_swapped_gates(bad_wires,gates):
    gates_to_swap = []
    all_bad_paths = []

    for bad_wire in bad_wires:
        gates_path = find_connected_gates(bad_wire,gates)
        all_bad_paths.append(gates_path)

    for path in range(all_bad_paths):
        for gate in path:
            for second_path in range(all_bad_paths):
                for second_gate in second_path:
                    file_path = "../data/24.txt"

                    single_wire_values, _ = parse_input_changed(file_path,)
                    new_single_wire_values = simulate_gates_switch(single_wire_values, gates, gate,second_gate)
                    result = compute_output(new_single_wire_values)

                    start_gate =
                    if result == 2**(j%45):
                        if i<45:
                            bad.append(f'x{i:02}')
                        else:
                            bad.append(f'y{i-45:02}')



    return gates_to_swap

if __name__ == "__main__":

    file_path = "../data/24.txt"
    wire_values, gates = parse_input(file_path)
    wire_values = simulate_gates(wire_values, gates)
    result = compute_output(wire_values)
    print(result)

    bad_bits = test_wrong()
    find_swapped_gates(bad_bits,gates)
    output_swaps(bad_bits,wire_values,gates)
