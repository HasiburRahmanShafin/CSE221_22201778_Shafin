
---

## lab1.py (LAB 1: File I/O, Sorting, and Manipulation)
```python
# LAB 1: File I/O, Sorting Algorithms, and Data Manipulation

# Task-1(a): Read numbers from file, classify even/odd
file = open('input1a.txt', 'r')
a = file.readline()
c = open("output1a.txt", "a")
for i in range(int(a)):
    new = int(file.readline())
    if new % 2 == 0:
        c.write(f"{new} is a even number\n")
    else:
        c.write(f"{new} is a odd number\n")
file.close()
c.close()

# Task-1(b): Evaluate arithmetic expressions from file
file = open("input1b.txt", "r")
a = file.readline()
out = open("output1b.txt", "a")
for line in file.readlines():
    eq = line.split()
    if eq[2] == "+":
        out.write(f"The result of {int(eq[1])} + {int(eq[3])} is {int(eq[1])+int(eq[3])}\n")
    elif eq[2] == "-":
        out.write(f"The result of {int(eq[1])} - {int(eq[3])} is {int(eq[1])-int(eq[3])}\n")
    elif eq[2] == "/":
        out.write(f"The result of {int(eq[1])} / {int(eq[3])} is {int(eq[1])/int(eq[3])}\n")
    elif eq[2] == "*":
        out.write(f"The result of {int(eq[1])} * {int(eq[3])} is {int(eq[1])*int(eq[3])}\n")
file.close()
out.close()

# Task-2: Bubble sort on a list (single array)
def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if int(arr[j]) > int(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

file = open("input2.txt", "r")
a = file.readline()
b = file.readline()
x = b.split()
out = open("output2.txt", "a")
c = bubbleSort(x)
for k in c:
    out.write(f"{k} ")
out.close()
file.close()

# Task-2 (alternate): Process multiple test cases from file
def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if int(arr[j]) > int(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

file = open("input2.txt", "r")
a = file.readlines()
out = open("output2.txt", "a")
for p in range(0, len(a), 2):
    b = a[p+1]
    x = b.split()
    c = bubbleSort(x)
    for k in c:
        out.write(f"{k} ")
out.close()
file.close()

# Task-3: Sort by marks (descending) and then by ID (ascending) using bubble sort
def bubbleSort(arr, b):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if int(arr[j]) < int(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                b[j], b[j+1] = b[j+1], b[j]
            if int(arr[j]) == int(arr[j+1]):
                if int(b[j]) > int(b[j+1]):
                    b[j], b[j+1] = b[j+1], b[j]
    return arr, b

file = open("input3.txt", "r")
out = open("output3.txt", "a")
file.readline()  # skip first line (number of students)
in1 = [int(x) for x in file.readline().split()]
in2 = [int(y) for y in file.readline().split()]
z = bubbleSort(in2, in1)
a, b = z[0], z[1]
for i in range(len(a)):
    out.write(f"ID: {b[i]} Mark: {a[i]}\n")
file.close()
out.close()

# Task-3 (using selection sort instead)
def selsort(a, b):
    for i in range(len(a)-1):
        min_idx = i
        for j in range(i, len(a)):
            if a[j] > a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        b[i], b[min_idx] = b[min_idx], b[i]
    # break ties for equal marks
    for k in range(len(a)-1):
        if a[k] == a[k+1]:
            for l in range(k+1, len(a)):
                if a[k] != a[l]:
                    break
                elif b[k] > b[l]:
                    b[k], b[l] = b[l], b[k]
    return a, b

file = open("input3.txt", "r")
out = open("output3.txt", "a")
file.readline()
in1 = [int(x) for x in file.readline().split()]
in2 = [int(y) for y in file.readline().split()]
a, b = selsort(in2, in1)
for i in range(len(a)):
    out.write(f"ID: {b[i]} Mark: {a[i]}\n")
file.close()
out.close()

# Task-4: Sort by name (alphabetical) then by time (earlier first)
file = open("input4.txt", "r")
out = open("output4.txt", "a")
l = file.readline()
a = []
for i in range(int(l)):
    a.append(file.readline().split())
# Bubble sort by name then time
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j][0] == a[j+1][0]:
            time1 = a[j][6].split(":")
            time2 = a[j+1][6].split(":")
            if (int(time1[0])*60 + int(time1[1])) < (int(time2[0])*60 + int(time2[1])):
                a[j], a[j+1] = a[j+1], a[j]
        elif ord(a[j][0][0]) > ord(a[j+1][0][0]):
            a[j], a[j+1] = a[j+1], a[j]
        elif ord(a[j][0][0]) == ord(a[j+1][0][0]):
            for k in range(len(a[j][0])):
                if k == len(a[j+1][0])-1:
                    a[j], a[j+1] = a[j+1], a[j]
                    break
                elif ord(a[j][0][k]) > ord(a[j+1][0][k]):
                    a[j], a[j+1] = a[j+1], a[j]
                    break
                elif ord(a[j][0][k]) != ord(a[j+1][0][k]):
                    break
for row in a:
    for col in row:
        out.write(f"{str(col)} ")
    out.write("\n")
file.close()
out.close()
