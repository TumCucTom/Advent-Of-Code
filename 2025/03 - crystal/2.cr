# Day 3, Part 2: Find maximum 12-digit joltage from each bank

def find_max_joltage(line : String, num_digits : Int32) : Int64
  # Greedy approach: at each position, pick the largest digit available
  # while ensuring we can still pick enough digits to reach num_digits total
  
  result = [] of Char
  start_idx = 0
  
  (0...num_digits).each do |pos|
    # We need to pick (num_digits - pos) more digits
    # So we can pick from start_idx to (line.size - (num_digits - pos))
    end_idx = line.size - (num_digits - pos) + 1
    
    # Find the maximum digit in the allowed range
    max_char = '0'
    max_idx = start_idx
    
    (start_idx...end_idx).each do |i|
      if line[i] > max_char
        max_char = line[i]
        max_idx = i
      end
    end
    
    result << max_char
    start_idx = max_idx + 1
  end
  
  # Convert result to integer
  result.join.to_i64
end

# Read input file
input_file = File.join(__DIR__, "..", "data", "3.txt")
lines = File.read_lines(input_file)

total = 0_i64
lines.each do |line|
  line = line.strip
  next if line.empty?
  max_joltage = find_max_joltage(line, 12)
  total += max_joltage
end

puts total
