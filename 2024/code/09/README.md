# Solution Explanation: Disk Fragmenter Problem

This solution solves the disk compaction problem by simulating two methods of file compaction and calculating the resulting checksum of the disk.

## Code Breakdown

1. **`pr(output)`**:
   This helper function prints the result and copies it to the clipboard using the `pyperclip` module.

2. **`compact_disk_by_file()`**:
   This function implements the file-by-file compaction method. It:
    - Parses the input disk map into `files` and `free_spaces` using a deque data structure.
    - Iterates through the disk map, storing the positions and sizes of files and free spaces.
    - Moves files from the end of the disk to the leftmost available free space, compacting them one file at a time.
    - After the compaction, it calculates the disk checksum by summing the product of each block's position and the file ID (skipping free spaces).

3. **Disk Parsing**:
    - The disk map is read and processed character by character, alternating between files and free spaces. Each file is assigned a unique ID, and the positions and sizes are recorded.

4. **File Compaction**:
    - Files are moved into the nearest available free space, starting from the last file and processing in reverse order.
    - The function ensures that files are moved only when there's sufficient free space available before their starting position.

5. **Checksum Calculation**:
    - Once the disk is compacted, the checksum is calculated by summing the product of each block's position and its file ID, excluding free space blocks.

6. **Result Output**:
    - The resulting checksum is printed and copied to the clipboard.

## Problem Models

- **Part One (File-by-File Compaction)**:
  In this part, files are moved one at a time to the leftmost available space. The process results in a compacted disk, and the checksum is calculated by summing the product of block positions and file IDs.

- **Part Two (Whole File Compaction)**:
  In this part, whole files are moved at once into the leftmost span of free space that can accommodate them. The process differs by considering entire files and trying to fit them into the free space in order of decreasing file ID.

