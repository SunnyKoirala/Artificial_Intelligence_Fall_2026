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


def dfs(start):

    # Stack
    stack = [start]

    # Visited set
    visited = set()

    traversal = []

    while stack:

        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        traversal.append(current)

        # Add neighbors to stack
        # reversed() gives a predictable traversal order
        for neighbor in reversed(graph[current]):

            if neighbor not in visited:
                stack.append(neighbor)

    return traversal


# Start DFS from A
result = dfs('A')

print("DFS Traversal Order:")
print(" -> ".join(result))