# Define the file path
file_path = 'Data/5.txt'

# Initialize lists
rules = []
changes = []

# Read the file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Process the first part (before the blank line)
for line in lines:
    if line.strip() == '':
        break
    x, y = map(int, line.strip().split('|'))  # Convert to integers
    rules.append((x, y))

# Process the second part (after the blank line)
for line in lines:
    line = line.strip()
    if line and '|' not in line:  # Ignore lines that don't contain arrays
        # Split the line by commas, convert each part to an integer, and add to the changes list
        array = list(map(int, line.split(',')))
        changes.append(array)

# Function to check if an array satisfies the conditions
def satisfies_condition(array, rules):
    for i, element in enumerate(array):
        # Get all pairs where the first number matches the current element (for the first condition)
        conflicting_rules = [y for x, y in rules if x == element]
        if any(conflict in array[:i] for conflict in conflicting_rules):
            return False
        
        # Get all pairs where the second number matches the current element (for the new condition)
        preceding_x_values = [x for x, y in rules if y == element]
        if any(x in array[i + 1:] for x in preceding_x_values):  # Check if any x appears after the current y
            return False
        
    return True

# Function to rearrange an array to satisfy the condition
def rearrange_array(array, rules):
    # Try to rearrange the array to make it satisfy the condition
    sorted_array = []
    remaining_elements = array[:]
    
    while remaining_elements:
        for element in remaining_elements:
            # Check if we can place this element while satisfying the condition
            conflicting_rules = [y for x, y in rules if x == element]
            preceding_x_values = [x for x, y in rules if y == element]
            
            # Check if the element can be safely placed in sorted_array
            if all(conflict not in sorted_array for conflict in conflicting_rules) and \
               all(x not in remaining_elements for x in preceding_x_values):
                sorted_array.append(element)
                remaining_elements.remove(element)
                break
        else:
            # If we can't find a valid element to place, return the unsorted array (error case)
            return array
    
    return sorted_array

# Total sum initialization
total_sum = 0

# Find arrays that do not satisfy the conditions and rearrange them
for array in changes:
    if not satisfies_condition(array, rules):
        rearranged_array = rearrange_array(array, rules)
        
        # Find the middle element in the rearranged array
        middle_index = len(rearranged_array) // 2
        middle_value = rearranged_array[middle_index]
        
        # Add the middle value to the total sum
        total_sum += middle_value

# Output the total sum
print(f"Total sum of middle values of rearranged arrays: {total_sum}")
