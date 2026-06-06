# LAB 4: Graph Representation (Adjacency Matrix and List)

import numpy as np

# Task-1(a): Read graph and store as adjacency matrix
file = open("input1.txt", "r")
out = open("output1a.txt", "a")
a, b = [int(i) for i in file.readline().split()]
matrix = [[0 for _ in range(int(a)+1)] for __ in range(int(a)+1)]
for _ in range(int(b)):
    x, y, z = [int(i) for i in file.readline().split()]
    matrix[x][y] = z
for row in matrix:
    for val in row:
        out.write(f"{val} ")
    out.write("\n")
out.close()
file.close()

# Task-1(b): Read graph and store as adjacency list (dictionary)
file = open("input1.txt", "r")
out = open("output1b.txt", "a")
a, b = [int(i) for i in file.readline().split()]
dic = {i: [] for i in range(int(a)+1)}
for _ in range(int(b)):
    x, y, z = [int(i) for i in file.readline().split()]
    dic[x].append((y, z))
for i, j in dic.items():
    out.write(f"{i} : ")
    for k in j:
        out.write(f"{k}")
    out.write("\n")
out.close()
file.close()

# Task-2: (Empty - no code provided)
