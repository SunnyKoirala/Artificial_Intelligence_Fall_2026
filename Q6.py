from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
queue = deque([start_node])
visited = {start_node}
traversal_order = []

while queue:
    node = queue.popleft()
    traversal_order.append(node)
    
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

print("BFS Traversal Order:", " -> ".join(traversal_order))
