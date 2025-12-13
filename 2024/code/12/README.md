# Solution Overview: Garden Groups

The code solves the problem of calculating the total cost of fencing regions in a garden map. Each region consists of adjacent garden plots with the same plant type. The cost is determined by multiplying the area of the region by its perimeter or the number of sides exposed.

## Approach:

1. **Input Parsing**:
    - The garden map is read from a text file where each garden plot is represented by a single letter, and adjacent plots of the same type form a region.

2. **Exploring Regions**:
    - The code uses a **Breadth-First Search (BFS)** algorithm to explore each unvisited cell in the grid and identify the connected region it belongs to.

3. **Area and Perimeter Calculation**:
    - **Area**: Count the number of plots in each region.
    - **Perimeter**: Check each neighboring plot to determine if it contributes to the perimeter. If a neighboring plot is out of bounds or has a different plant type, it contributes to the perimeter.

4. **Counting Sides**:
    - A set of directions is used to track the unique sides of the region that form the perimeter.

5. **Cost Calculation**:
    - For each region, the price is calculated as `Area * Sides`.
    - The total cost is accumulated by summing the price of each region.

6. **Final Output**:
    - The total fencing cost is printed and copied to the clipboard.

## Code Workflow:

- **Grid Setup**: The input grid is processed into rows and columns.
- **Region Identification**: For each unvisited plot, BFS is initiated to explore and mark all plots in the region.
- **Perimeter Calculation**: For each region, the unique perimeter sides are counted using the directions set.
- **Price Calculation**: The price for each region is computed and added to the total.

## Code Efficiency:
- **Recursion Limit**: The recursion limit is increased to handle large grids.
- **Visited Set**: A set is used to track visited plots to ensure each plot is processed only once.

