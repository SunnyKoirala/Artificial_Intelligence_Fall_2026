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

heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 2,
    'E': 3,
    'F': 2,
    'G': 0
}


def best_first_search(start, goal):

    queue = []

    heapq.heappush(
        queue,
        (heuristic[start], start)
    )

    visited = set()

    while queue:

        h, node = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)

        print("Visited:", node)

        if node == goal:
            print("Goal Reached")
            return

        for neighbor in graph[node]:

            if neighbor not in visited:

                heapq.heappush(
                    queue,
                    (heuristic[neighbor], neighbor)
                )

    print("Goal Not Found")


best_first_search('A', 'G')