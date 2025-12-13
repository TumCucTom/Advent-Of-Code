
# Solution Explanation for Advent of Code 2024 - Day 22: Monkey Market

The code simulates a series of operations for each buyer in the Monkey Exchange Market to predict their prices based on a pseudorandom sequence. It then identifies the sequence of price changes that maximizes the total number of bananas.

## Key Functions and Concepts:

### 1. **Mixing and Pruning Values**
The core of the problem involves generating secret numbers through a sequence of operations. Each operation mixes and prunes values to produce a new secret number. This process involves:
- Multiplying the secret number by 64, XORing with the current secret, and pruning.
- Dividing the secret by 32, XORing with the result, and pruning.
- Multiplying the secret by 2048, XORing, and pruning again.

These steps are repeated 2000 times to generate a sequence of secret numbers for each buyer.

### 2. **Extracting Price Changes**
Once the sequence of secret numbers is generated, the prices are derived from the last digit of each secret number. The code calculates the changes between consecutive prices to identify patterns that the monkey can use to decide when to sell.

### 3. **Pattern Matching**
The main goal is to find a specific sequence of four consecutive changes in prices that maximizes the total bananas the monkey gets. The code identifies these sequences and tracks the maximum score by accumulating the values of each identified pattern.

### 4. **Accumulates Scores**
The code uses the changes between consecutive values to identify patterns. It keeps track of how often each pattern occurs and accumulates the corresponding score, ultimately finding the maximum score.

### 5. **Result Calculation**
Once all patterns are processed, the code calculates the maximum score and prints it, both to the console and copies it to the clipboard for convenience.

---

## How the Code Solves the Problem:

1. **Input Processing**:
   The code reads a list of initial secret numbers from the input file.

2. **Sequence Generation**:
   For each secret number, the code generates 2000 new secret numbers using the mixing and pruning functions.

3. **Price Change Calculation**:
   It calculates the changes in price by looking at the last digit of each secret number and finding the differences between consecutive prices.

4. **Pattern Recognition**:
   The code looks for patterns of four consecutive price changes and stores the resulting score.

5. **Accumulate and Compare**:
   The scores are accumulated in a dictionary, and the highest score is identified.

6. **Output**:
   The code prints and copies the highest accumulated score, which corresponds to the maximum bananas the monkey can get by following the identified sequence of price changes.

By simulating the sequence generation and identifying the optimal price change sequence, the code provides the solution to the problem as required by the puzzle.
