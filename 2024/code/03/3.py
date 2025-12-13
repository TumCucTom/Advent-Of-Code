import re

# Function to process the text file and calculate the total sum
def calculate_total_sum(file_path):
    total_sum = 0
    # Define the regex pattern for mul(x,y), do(), and don't()
    mul_pattern = r"mul\((-?\d+),(-?\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don['’]t\(\)"
    
    # A flag to control the state (whether we are looking for 'mul' or 'do')
    looking_for_mul = True
    
    # Open the text file
    with open(file_path, 'r') as file:
        content = file.read()  # Read the entire content of the file

    # Remove all newline characters to treat the entire content as one continuous string
    content = content.replace("\n", "")  # or content.replace("\n", " ") if you want spaces instead of no break

    # Iterate through the content letter by letter
    i = 0
    while i < len(content):
        # Check for 'don't()' and stop looking for 'mul' when found
        if looking_for_mul and re.match(dont_pattern, content[i:]):
            looking_for_mul = False
            i += len("don't()")  # Move the index forward by the length of "don't()"
            continue

        # Check for 'do()' and start looking for both 'mul' and 'don't()'
        if not looking_for_mul and re.match(do_pattern, content[i:]):
            looking_for_mul = True
            i += len("do()")  # Move the index forward by the length of "do()"
            continue

        # If we are looking for 'mul' and it's found, process it
        if looking_for_mul:
            match = re.match(mul_pattern, content[i:])
            if match:
                x = int(match.group(1))
                y = int(match.group(2))
                total_sum += x * y
                i += len(match.group(0))  # Move the index forward by the length of "mul(x,y)"
                continue

        # Move to the next character if no matches are found
        i += 1

    # Print the final total sum
    print(f"Total sum: {total_sum}")

# Example usage
file_path = 'Data/3.txt'  # Replace with the path to your text file
calculate_total_sum(file_path)
