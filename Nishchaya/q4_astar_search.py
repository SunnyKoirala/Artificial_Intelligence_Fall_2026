import heapq

def a_star_search(graph, heuristics, start='A', goal='G'):
    print("=" * 60)
    print("QUESTION 4: A* SEARCH ALGORITHM")
    print("=" * 60)
    print(f"Start Node: {start} | Goal Node: {goal}\n")

    pq = []
    initial_f = 0 + heuristics[start]
    heapq.heappush(pq, (initial_f, 0, start, [start]))

    g_scores = {start: 0}
    
    print("A* Exploration Steps:")
    print("-" * 50)
    step = 1

    while pq:
        f, g, current, path = heapq.heappop(pq)

        print(f"  Step {step:2d}: Popped '{current}' | Path: {' -> '.join(path)} | g={g}, h={heuristics[current]}, f={f}")
        step += 1

        if current == goal:
            print("-" * 50)
            print("\nOptimal Path Found!")
            print(f"  - Optimal Path: {' -> '.join(path)}")
            print(f"  - Total Cost:   {g}")
            print("=" * 60)
            return path, g

        for neighbor, weight in graph.get(current, []):
            tentative_g = g + weight
            
            if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g
                h = heuristics[neighbor]
                f_score = tentative_g + h
                heapq.heappush(pq, (f_score, tentative_g, neighbor, path + [neighbor]))

    print("-" * 50)
    print("\nNo path found to goal.")
    print("=" * 60)
    return None, float('inf')

def main():
    graph = {
        'A': [('B', 2), ('C', 4)],
        'B': [('D', 7), ('E', 3)],
        'C': [('E', 1), ('F', 6)],
        'D': [('G', 3)],
        'E': [('G', 2)],
        'F': [('G', 4)],
        'G': []
    }

    heuristics = {
        'A': 6,
        'B': 4,
        'C': 4,
        'D': 3,
        'E': 2,
        'F': 3,
        'G': 0
    }

    a_star_search(graph, heuristics, start='A', goal='G')

if __name__ == "__main__":
    main()
