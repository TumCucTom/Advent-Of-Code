import sys
import pyperclip as pc
from collections import deque

def pr(output):
    """Prints the output and copies it to the clipboard."""
    print(output)
    pc.copy(output)

sys.setrecursionlimit(10**6)
infile = '../data/9.txt'
disk_map = open(infile).read().strip()

def compact_disk_by_file():
    """
    Solves the disk compaction problem (file-by-file compaction).
    """
    files = deque([])  # Stores files as (start_position, size, file_id)
    free_spaces = deque([])  # Stores free space as (start_position, size)
    file_id = 0  # ID for each file
    final_disk = []  # Representation of the disk after compaction
    position = 0  # Current position on the disk

    # Parse the disk map into files and free spaces
    for i, char in enumerate(disk_map):
        if i % 2 == 0:  # File segment
            files.append((position, int(char), file_id))
            for _ in range(int(char)):
                final_disk.append(file_id)  # Add the file ID to the disk
                position += 1
            file_id += 1
        else:  # Free space segment
            free_spaces.append((position, int(char)))
            for _ in range(int(char)):
                final_disk.append(None)  # Add free space to the disk
                position += 1

    # Process files in reverse order for compaction
    for (start_pos, size, file_id) in reversed(files):
        for space_idx, (space_pos, space_size) in enumerate(free_spaces):
            if space_pos < start_pos and size <= space_size:
                # Move the file into the free space
                for i in range(size):
                    assert final_disk[start_pos + i] == file_id, f'{final_disk[start_pos + i]=}'
                    final_disk[start_pos + i] = None  # Clear the old position
                    final_disk[space_pos + i] = file_id  # Place file in the free space
                # Update the free space
                free_spaces[space_idx] = (space_pos + size, space_size - size)
                break

    # Calculate the checksum
    checksum = 0
    for i, block in enumerate(final_disk):
        if block is not None:
            checksum += i * block
    return checksum

# Solve for file-by-file compaction
disk_checksum = compact_disk_by_file()  # File-by-file compaction
pr(disk_checksum)  # Print and copy the result
