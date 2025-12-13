def read_matrix_from_file(file_path):
    matrix = []

    with open(file_path, 'r') as file:
        for line in file:
            # Convert the line into a list of numbers
            row = list(map(float, line.split()))
            matrix.append(row)

    return matrix


def is_valid_row(row):
    # Check if the row is strictly increasing or strictly decreasing
    is_increasing = all(row[i] < row[i + 1] for i in range(len(row) - 1))
    is_decreasing = all(row[i] > row[i + 1] for i in range(len(row) - 1))

    # If neither increasing nor decreasing, it's invalid
    if not is_increasing and not is_decreasing:
        return False

    # Check if all consecutive differences are between 1 and 3 (inclusive)
    differences = [abs(row[i + 1] - row[i]) for i in range(len(row) - 1)]
    return all(1 <= diff <= 3 for diff in differences)


def count_valid_rows(file_path):
    matrix = read_matrix_from_file(file_path)
    valid_row_count = 0

    for row in matrix:
        # Check if the row without any removal is valid
        if is_valid_row(row):
            valid_row_count += 1
        else:
            # Try removing one number from the row and check if it becomes valid
            for i in range(len(row)):
                modified_row = row[:i] + row[i + 1:]
                if is_valid_row(modified_row):
                    valid_row_count += 1
                    break  # Only need to find one valid modification

    return valid_row_count


# Example usage
file_path = "Data/2.txt"  # Replace with the path to your file
result = count_valid_rows(file_path)
print(f"Count of valid rows: {result}")
