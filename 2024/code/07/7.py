from itertools import product

# Function to evaluate a given expression based on the provided operators
def evaluate_expression(numbers, operators):
    result = int(numbers[0])  # Start with the first number
    
    for i, op in enumerate(operators):
        if op == '+':
            result += int(numbers[i + 1])
        elif op == '*':
            result *= int(numbers[i + 1])
        elif op == '||':
            # Concatenate the two numbers as strings and convert back to an integer
            result = int(str(result) + str(numbers[i + 1]))
    
    return result

# Function to determine the total calibration result by checking which equations are valid
def find_possible_true_equations(file_path):
    # Read the input data from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    total_calibration_result = 0
    
    for line in lines:
        # Split the line into the test value and the numbers
        parts = line.strip().split(":")
        test_value = int(parts[0].strip())
        numbers = list(map(int, parts[1].strip().split()))
        
        # Generate all combinations of operators (+, *, ||)
        num_operators = len(numbers) - 1
        operator_combinations = product(['+', '*', '||'], repeat=num_operators)
        
        # Check each combination of operators
        valid_equation = False
        for operators in operator_combinations:
            if evaluate_expression(numbers, operators) == test_value:
                valid_equation = True
                break
        
        # If the equation is valid, add the test value to the result
        if valid_equation:
            total_calibration_result += test_value
    
    return total_calibration_result

# Test with the example file "Data/7.txt"
total_calibration = find_possible_true_equations("../Data/7.txt")
print(total_calibration)
