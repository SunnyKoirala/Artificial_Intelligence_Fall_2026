from collections import deque

# Graph represented using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}


def bfs(start):

    # Queue
    queue = deque()

    # Set to store visited nodes
    visited = set()

    queue.append(start)
    visited.add(start)

    traversal = []

    while queue:

        current = queue.popleft()

        traversal.append(current)

        # Visit neighbors
        for neighbor in graph[current]:

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal


# Start BFS from A
result = bfs('A')

print("BFS Traversal Order:")
print(" -> ".join(result))