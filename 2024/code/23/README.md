
# Solution Explanation for Day 23: LAN Party

## Problem Overview

The task involves finding the largest group of interconnected computers from a network map. The problem asks for two main parts:

1. **Part 1**: Find all sets of three interconnected computers that contain at least one computer with a name starting with "t".
2. **Part 2**: Identify the largest set of computers that are all connected to each other (i.e., a clique), and output their names sorted alphabetically as the password.

## Code Breakdown

### 1. **Reading and Preparing the Data**

The network map, provided as input, consists of bidirectional connections between computers. The code reads this data and builds an adjacency list where each computer is a key, and its connected computers are stored as a set of values.

```python
with open(input_file, "r") as file:
    connections = file.read().strip().split("\n")
```

The adjacency list is created from these connections:

```python
adj_list = defaultdict(set)
for connection in connections:
    a, b = connection.split("-")
    adj_list[a].add(b)
    adj_list[b].add(a)
```

### 2. **Finding Cliques Using Bron-Kerbosch Algorithm**

The Bron-Kerbosch algorithm is used to find all maximal cliques in the graph. A clique is a subset of computers where every computer is connected to every other computer in the subset.

```python
def bron_kerbosch(r, p, x, adj_list):
    if not p and not x:
        yield r
    while p:
        v = p.pop()
        yield from bron_kerbosch(r.union({v}), p.intersection(adj_list[v]), x.intersection(adj_list[v]), adj_list)
        x.add(v)
```

### 3. **Finding the Largest Clique**

The `bron_kerbosch` function is used to generate all maximal cliques, and the largest one is selected using the `max` function:

```python
all_nodes = set(adj_list.keys())
largest_clique = max(bron_kerbosch(set(), all_nodes, set(), adj_list), key=len)
```

### 4. **Output**

The largest clique is then sorted alphabetically and joined with commas to form the password, which is both printed and copied to the clipboard:

```python
password = ",".join(sorted(largest_clique))
print(password)
pyperclip.copy(password)
```

## Solution to the Problem

- **Part 1**: The task involves counting sets of three computers that are interconnected and contain at least one computer starting with "t".
- **Part 2**: The task is to find the largest clique of connected computers and output the sorted names as the password.

### Conclusion

The code successfully solves the problem by constructing an adjacency list from the input data, applying the Bron-Kerbosch algorithm to find maximal cliques, and selecting the largest clique as the password.