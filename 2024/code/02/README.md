### Solution Overview

#### Part 1:
Reads the matrix from a file, checks each row for validity based on two conditions:
1. The row must be strictly increasing or decreasing.
2. The differences between consecutive elements must be between 1 and 3.
#### Part 2:
Same as above but runs every row of the matrix with an item removed until it's still found invalid or a valid row is made by removing one item.