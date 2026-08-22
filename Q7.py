graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
stack = [start_node]
visited = set()
traversal_order = []

while stack:
    node = stack.pop()
    
    if node not in visited:
        visited.add(node)
        traversal_order.append(node)
        
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(neighbor)

print("DFS Traversal Order:", " -> ".join(traversal_order))
