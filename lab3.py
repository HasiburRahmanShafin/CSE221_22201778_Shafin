# LAB 3: Merge Sort and Recursion

# Task-1: Merge Sort implementation
def merge(a, b):
    # a and b are sorted lists
    i, j, k = 0, 0, 0
    arr = [0] * (len(a) + len(b))
    while i <= len(arr)-1:
        if j >= len(a):
            arr[i] = b[k]
            k += 1
        elif k >= len(b):
            arr[i] = a[j]
            j += 1
        elif a[j] <= b[k]:
            arr[i] = a[j]
            j += 1
        else:
            arr[i] = b[k]
            k += 1
        i += 1
    return arr

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    a1 = mergeSort(arr[0:mid])
    a2 = mergeSort(arr[mid:])
    return merge(a1, a2)

# Example usage (commented):
# inp = [1, 2, 3, 4, 5, 6, 9, 9]
# print(mergeSort(inp))

# Task-2: Max point (incomplete - placeholder)
def maxpoint(ar1, ar2):
    i = j = 0
    max_val = 0
    # The function is incomplete; left as in original notebook.
    pass

def mergeSort2(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    a1 = mergeSort2(arr[0:mid])
    a2 = mergeSort2(arr[mid+1:])  # Note: mid+1 might cause index error; kept as original
    return maxpoint(a1, a2)       # placeholder
