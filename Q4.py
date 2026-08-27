import heapq

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3), ('E', 8)],
    'C': [('F', 5)],
    'D': [('G', 9)],
    'E': [('G', 2)],
    'F': [('G', 4)],
    'G': []
}

heuristics = {
    'A': 10,
    'B': 8,
    'C': 7,
    'D': 6,
    'E': 2,
    'F': 3,
    'G': 0
}

start_node = 'A'
goal_node = 'G'

pq = [(heuristics[start_node], 0, start_node, [start_node])]
visited = {}

found = False
while pq:
    f, g, current, path = heapq.heappop(pq)
    
    if current in visited and visited[current] <= g:
        continue
    visited[current] = g
    
    if current == goal_node:
        print("Optimal Path:", " -> ".join(path))
        print("Total Cost:", g)
        found = True
        break
        
    for neighbor, weight in graph.get(current, []):
        new_g = g + weight
        new_f = new_g + heuristics.get(neighbor, 0)
        heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

if not found:
    print("No path found.")
