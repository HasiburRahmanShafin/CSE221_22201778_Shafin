# LAB 2: Two-Pointer Technique, Merging Sorted Arrays, Activity Selection

# Task-1: Find pair with given sum using two pointers
file = open("input1.txt", "r")
out = open("output1.txt", "a")
a = file.readline().split()
lis = [int(x) for x in file.readline().split()]
target = int(a[1])
x, y = 0, len(lis)-1
result = False
while x < y:
    s = lis[x] + lis[y]
    if s < target:
        x += 1
    elif s > target:
        y -= 1
    else:
        out.write(f"{x+1} {y+1}")
        result = True
        break
if not result:
    out.write("IMPOSSIBLE")
file.close()
out.close()

# Task-2: Merge two sorted arrays
file = open("input2.txt", "r")
out = open("output2.txt", "a")
a = int(file.readline())
lisa = file.readline().split()
b = int(file.readline())
lisb = file.readline().split()
i, j = 0, 0
while i < a or j < b:
    if i == a:
        out.write(f"{int(lisb[j])} ")
        j += 1
    elif j == b:
        out.write(f"{int(lisa[i])} ")
        i += 1
    elif int(lisa[i]) < int(lisb[j]):
        out.write(f"{int(lisa[i])} ")
        i += 1
    else:
        out.write(f"{int(lisb[j])} ")
        j += 1
out.close()
file.close()

# Task-3: Activity selection (maximum number of non-overlapping intervals)
file = open("input3.txt", "r")
out = open("output3.txt", "a")
sum_max = 0
ans = ""
lis = []
for _ in range(int(file.readline())):
    lis.append(file.readline().split())
# Sort by start time, then by end time (ascending)
for m in range(len(lis)-1):
    for n in range(len(lis)-1):
        if int(lis[n][0]) > int(lis[n+1][0]):
            lis[n], lis[n+1] = lis[n+1], lis[n]
        elif int(lis[n][0]) == int(lis[n+1][0]) and int(lis[n][1]) > int(lis[n+1][1]):
            lis[n], lis[n+1] = lis[n+1], lis[n]
# Greedy activity selection
for j in range(len(lis)):
    test_sum = 1
    test_ans = f"{lis[j][0]} {lis[j][1]}"
    test_point = int(lis[j][1])
    for k in range(len(lis)):
        suru, sesh = lis[k]
        if j != k and int(suru) >= test_point:
            test_point = int(sesh)
            test_ans += f"{suru} {sesh}"
            test_sum += 1
    if test_sum > sum_max:
        sum_max = test_sum
        ans = test_ans
out.write(f"{sum_max}\n{ans}")
file.close()
out.close()

# Task-4: Activity selection (same as Task-3) - file names adjusted
file = open("input4.txt", "r")
out = open("output4.txt", "a")
sum_max = 0
lis = []
for _ in range(int(file.readline())):
    lis.append(file.readline().split())
# Sort by start time, then by end time (ascending)
for m in range(len(lis)-1):
    for n in range(len(lis)-1):
        if int(lis[n][0]) > int(lis[n+1][0]):
            lis[n], lis[n+1] = lis[n+1], lis[n]
        elif int(lis[n][0]) == int(lis[n+1][0]) and int(lis[n][1]) > int(lis[n+1][1]):
            lis[n], lis[n+1] = lis[n+1], lis[n]
# Greedy activity selection
for j in range(len(lis)):
    test_sum = 1
    test_ans = f"{lis[j][0]} {lis[j][1]}"
    test_point = int(lis[j][1])
    for k in range(len(lis)):
        suru, sesh = lis[k]
        if j != k and int(suru) >= test_point:
            test_point = int(sesh)
            test_ans += f"{suru} {sesh}"
            test_sum += 1
    if test_sum > sum_max:
        sum_max = test_sum
        ans = test_ans
out.write(f"{sum_max}\n{ans}")
file.close()
out.close()

# Lab Quiz: Bubble sort with limited swaps to check if array can be sorted
file = open("input.txt", "r")
out = open("output.txt", "a")
l = file.readline().split()
k = int(file.readline())
# Perform up to k swaps (bubble sort style)
for i in range(len(l)-1):
    for j in range(len(l)-1):
        if int(l[j]) > int(l[j+1]) and k != 0:
            l[j], l[j+1] = l[j+1], l[j]
            k -= 1
result = "yeas"
for idx in range(len(l)-1):
    if int(l[idx]) > int(l[idx+1]):
        result = "Noh"
out.write(result)
file.close()
out.close()
