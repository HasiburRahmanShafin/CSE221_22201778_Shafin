# LAB 5: Topological Sort using DFS and BFS (Kahn's Algorithm)

# Task-1(a): DFS-based topological sort
input_file = open('input1a.txt', "r")
output_file = open('output1a.txt', "w")
n, m = [int(i) for i in input_file.readline().split()]
graph = [[] for _ in range(n+1)]
inDeg = [0] * (n+1)
for _ in range(m):
    x, y = [int(i) for i in input_file.readline().split()]
    graph[x].append(y)
    inDeg[y] += 1

def dfs(G, v, visited, inDeg, result):
    visited.append(v)
    result.append(v)
    for element in G[v]:
        inDeg[element] -= 1
        if element not in visited and inDeg[element] == 0:
            dfs(G, element, visited, inDeg, result)

def topSortDFS(graph, inDeg, node, output_file):
    result = []
    visited = []
    for i in range(1, len(graph)):
        if inDeg[i] == 0 and i not in visited:
            dfs(graph, i, visited, inDeg, result)
    if len(result) < node:
        output_file.write('IMPOSSIBLE\n')
    else:
        for i in result:
            output_file.write(str(i) + " ")

topSortDFS(graph, inDeg, n, output_file)
input_file.close()
output_file.close()

# Task-1(b): BFS-based topological sort (Kahn's algorithm)
def graphRepAdjList(input_file):
    n, m = tuple(map(int, input_file.readline().split()))
    graph = [[] for _ in range(n+1)]
    inDeg = [0] * (n+1)
    for _ in range(m):
        u, v = tuple(map(int, input_file.readline().split()))
        graph[u].append(v)
        inDeg[v] += 1
    return graph, inDeg, n

def bfs(G, v, visited, result, Q, inDeg):
    visited.append(v)
    Q.append(v)
    while Q:
        x = Q.pop(0)
        result.append(x)
        for adj in G[x]:
            inDeg[adj] -= 1
            if adj not in visited and inDeg[adj] == 0:
                visited.append(adj)
                Q.append(adj)

def topSortBFS(graph, inDeg, node, output_file):
    result = []
    visited = []
    Q = []
    for i in range(1, len(graph)):
        if inDeg[i] == 0 and i not in visited:
            bfs(graph, i, visited, result, Q, inDeg)
    if len(result) < node:
        output_file.write('IMPOSSIBLE\n')
    else:
        for i in result:
            output_file.write(str(i) + " ")

input_path = 'input1b.txt'
output_path = 'output1b.txt'
input_file = open(input_path, "r")
output_file = open(output_path, "w")
graph, inDeg, node = graphRepAdjList(input_file)
topSortBFS(graph, inDeg, node, output_file)
input_file.close()
output_file.close()
