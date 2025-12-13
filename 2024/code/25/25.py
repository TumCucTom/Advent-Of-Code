import pyperclip  # Ensure you have the pyperclip module installed

def parse_schematics(file_path):
    with open(file_path, 'r') as f:
        data = f.read().strip().split("\n\n")

    locks, keys = [], []
    for schematic in data:
        rows = schematic.splitlines()
        if rows[0] == "#####":  # It's a lock
            locks.append(rows)
        elif rows[-1] == "#####":  # It's a key
            keys.append(rows)
    return locks, keys

def calculate_heights(schematic, is_lock):
    num_columns = len(schematic[0])
    heights = []
    total_height = len(schematic)

    for col in range(num_columns):
        height = 0
        if is_lock:  # Measure downward
            for row in range(total_height):
                if schematic[row][col] == '#':
                    height += 1
                else:
                    break
        else:  # Measure upward
            for row in range(total_height - 1, -1, -1):
                if schematic[row][col] == '#':
                    height += 1
                else:
                    break
        heights.append(height)
    return heights

def count_compatible_pairs(locks, keys):
    total_height = len(locks[0])  # Assumed constant
    compatible_pairs = 0

    for lock in locks:
        lock_heights = calculate_heights(lock, is_lock=True)
        for key in keys:
            key_heights = calculate_heights(key, is_lock=False)
            if all(lh + kh <= total_height for lh, kh in zip(lock_heights, key_heights)):
                compatible_pairs += 1
    return compatible_pairs

# Main Execution
file_path = '../../data/25.txt'  # Replace with your input file path
locks, keys = parse_schematics(file_path)
result = count_compatible_pairs(locks, keys)

# Print and copy result to clipboard
print(f"Number of compatible lock/key pairs: {result}")
pyperclip.copy(str(result))  # Copies the result to the clipboard
