import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
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

pq = [(heuristics[start_node], start_node)]
visited = set()

while pq:
    h, current = heapq.heappop(pq)
    
    if current in visited:
        continue
        
    visited.add(current)
    print("Visited node:", current)
    
    if current == goal_node:
        print("Goal Reached")
        break
        
    for neighbor in graph.get(current, []):
        if neighbor not in visited:
            heapq.heappush(pq, (heuristics[neighbor], neighbor))
