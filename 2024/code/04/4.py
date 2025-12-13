def is_valid_position(r, c):
        return 0 <= r < rows and 0 <= c < cols

def check_diags(r,c, grid):
    diag_num = 0
    if grid[r-1][c-1] == "M":
        if grid[r+1][c+1] == "S":
            diag_num +=1
    if grid[r-1][c+1] == "M":
        if grid[r+1][c-1] == "S":
            diag_num +=1
    if grid[r+1][c-1] == "M":
        if grid[r-1][c+1] == "S":
            diag_num +=1
    if grid[r+1][c+1] == "M":
        if grid[r-1][c-1] == "S":
            diag_num +=1
            
    return diag_num

def matches_pattern(r,c, grid):
    """Check if the 'MAS' pattern matches starting at (r, c)."""
    try:
        return check_diags(r,c, grid) == 2        
    except IndexError:
        return False


def count_xmas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Iterate through each cell in the grid as the center
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "A":
                continue  # Center must be 'A'
            if matches_pattern(r,c,grid):
                count += 1

    return count


# Read the grid from the file
file_path = "Data/4.txt"
try:
    with open(file_path, "r") as file:
        grid = [list(line.strip()) for line in file if line.strip()]
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()

# Count X-MAS patterns
result = count_xmas_patterns(grid)
print("Number of X-MAS patterns:", result)
