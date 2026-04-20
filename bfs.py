#bfs
from collections import deque

graph = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start = input("Enter starting node: ")
q = deque([start])
visited = set()
visited.add(start)

print("BFS Traversal:")

while q:
    node = q.popleft()
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            q.append(neighbor)