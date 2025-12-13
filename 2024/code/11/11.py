
import pyperclip as pc

# Function to transform stones and keep track of their counts efficiently
def transform_stones_count(stones_count):
    new_stones_count = {}

    for stone, count in stones_count.items():
        # Case 1: If the stone is 0, it becomes 1
        if stone == 0:
            new_stones_count[1] = new_stones_count.get(1, 0) + count
        # Case 2: If the stone has an even number of digits, split it
        elif len(str(stone)) % 2 == 0:
            # Split the stone into two parts
            str_stone = str(stone)
            mid = len(str_stone) // 2
            left = int(str_stone[:mid])
            right = int(str_stone[mid:])

            new_stones_count[left] = new_stones_count.get(left, 0) + count
            new_stones_count[right] = new_stones_count.get(right, 0) + count
        # Case 3: Otherwise, multiply the stone by 2024
        else:
            new_stones_count[stone * 2024] = new_stones_count.get(stone * 2024, 0) + count

    return new_stones_count

# Function to simulate the blinks for a given number of times
def simulate_blinks(initial_stones, num_blinks):
    # Create a dictionary to keep track of the counts of each stone
    stones_count = {}
    for stone in initial_stones:
        stones_count[stone] = stones_count.get(stone, 0) + 1

    # Apply the transformation rules for each blink
    for _ in range(num_blinks):
        stones_count = transform_stones_count(stones_count)

    # The total number of stones is the sum of the counts
    total_stones = sum(stones_count.values())
    pc.copy(str(total_stones))  # Copy the result to the clipboard
    return total_stones

# Reading the input from the file
def read_input(file_path):
    with open(file_path, 'r') as file:
        # Read the first line, convert it into a list of integers (the stones)
        stones = list(map(int, file.read().strip().split()))
    return stones

# Main function to run the program
def main():
    # Read the initial stones from the file
    initial_stones = read_input("../data/11.txt")

    # Number of blinks (now 75 instead of 25)
    num_blinks = 75

    # Get the number of stones after 75 blinks and print the result
    result = simulate_blinks(initial_stones, num_blinks)
    print(f"Total number of stones after {num_blinks} blinks: {result}")

if __name__ == "__main__":
    main()
