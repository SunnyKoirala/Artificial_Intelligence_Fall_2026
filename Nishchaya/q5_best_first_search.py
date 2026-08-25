import heapq

def greedy_best_first_search(graph, heuristics, start='A', goal='G'):
    print("=" * 60)
    print("QUESTION 5: GREEDY BEST FIRST SEARCH")
    print("=" * 60)
    print(f"Start Node: {start} | Goal Node: {goal}\n")

    pq = []
    heapq.heappush(pq, (heuristics[start], start, [start]))

    visited = set()
    visited_order = []

    print("Visited Nodes during Search:")
    print("-" * 40)

    while pq:
        h, current, path = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)
        visited_order.append(current)
        print(f"  Visited Node: '{current}' (Heuristic h = {h})")

        if current == goal:
            print("-" * 40)
            print("Goal Reached!")
            print(f"  - Visited Sequence: {' -> '.join(visited_order)}")
            print(f"  - Traversed Path:   {' -> '.join(path)}")
            print("=" * 60)
            return path

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristics[neighbor], neighbor, path + [neighbor]))

    print("-" * 40)
    print("Goal Not Reached.")
    print("=" * 60)
    return None

def main():

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
        'A': 6,
        'B': 4,
        'C': 3,
        'D': 5,
        'E': 1,
        'F': 2,
        'G': 0
    }

    greedy_best_first_search(graph, heuristics, start='A', goal='G')

if __name__ == "__main__":
    main()
