def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # Add neighbors in reverse order
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Example graph (adjacency list)
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I'],
    'E': ['J', 'K'],
    'F': [],
    'G': ['L'],
    'H': [],
    'I': ['M'],
    'J': [],
    'K': ['N'],
    'L': [],
    'M': [],
    'N': []
}

print("DFS Traversal:")
dfs(graph, 'A')
