import heapq

# --------------------------------------------------
# A* Search Algorithm
# --------------------------------------------------

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('E', 1)],
    'D': [('B', 2), ('G', 1)],
    'E': [('B', 5), ('C', 1), ('G', 2)],
    'G': [('D', 1), ('E', 2)]
}


# Heuristic values
heuristic = {
    'A': 4,
    'B': 3,
    'C': 3,
    'D': 1,
    'E': 2,
    'G': 0
}


def a_star(start, goal):

    # Priority queue:
    # (f_cost, g_cost, node, path)
    priority_queue = []

    heapq.heappush(
        priority_queue,
        (heuristic[start], 0, start, [start])
    )

    visited = set()

    while priority_queue:

        f, g, current, path = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        # Goal reached
        if current == goal:
            return path, g

        # Explore neighbors
        for neighbor, cost in graph[current]:

            if neighbor not in visited:

                new_g = g + cost
                new_f = new_g + heuristic[neighbor]

                heapq.heappush(
                    priority_queue,
                    (
                        new_f,
                        new_g,
                        neighbor,
                        path + [neighbor]
                    )
                )

    return None, float('inf')


# Run A*
path, cost = a_star('A', 'G')

if path:
    print("Optimal Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found.")