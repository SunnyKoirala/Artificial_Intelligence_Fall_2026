import heapq

# Graph represented as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 2,
    'E': 3,
    'F': 4,
    'G': 0
}


def greedy_best_first_search(start, goal):

    # Priority queue based only on heuristic h(n)
    priority_queue = []

    heapq.heappush(
        priority_queue,
        (heuristic[start], start)
    )

    visited = set()

    while priority_queue:

        h, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        print("Visited:", current)

        # Goal check
        if current == goal:
            print("Goal Reached")
            return

        # Add neighbors
        for neighbor in graph[current]:

            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbor], neighbor)
                )

    print("Goal Not Found")


# Run search
greedy_best_first_search('A', 'G')