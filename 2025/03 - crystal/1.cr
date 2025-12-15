# Day 3, Part 1: Find maximum 2-digit joltage from each bank

def find_max_joltage(line : String, num_digits : Int32) : Int64
  # For 2 digits, find the maximum pair
  max_joltage = 0_i64
  
  (0...line.size).each do |i|
    ((i + 1)...line.size).each do |j|
      joltage = (line[i].to_s + line[j].to_s).to_i64
      max_joltage = joltage if joltage > max_joltage
    end
  end
  
  max_joltage
end

# Read input file
input_file = File.join(__DIR__, "..", "data", "3.txt")
lines = File.read_lines(input_file)

total = 0_i64
lines.each do |line|
  line = line.strip
  next if line.empty?
  max_joltage = find_max_joltage(line, 2)
  total += max_joltage
end

puts total
