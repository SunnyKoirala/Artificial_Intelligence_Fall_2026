from collections import deque

def bfs_traversal(graph, start_node='A'):
    print("=" * 60)
    print("QUESTION 6: BREADTH FIRST SEARCH (BFS) TRAVERSAL")
    print("=" * 60)
    print(f"Start Node: {start_node}\n")

    queue = deque([start_node])
    visited = set([start_node])
    traversal_order = []

    print("BFS Traversal Steps:")
    print("-" * 40)

    while queue:
        current = queue.popleft()
        traversal_order.append(current)
        print(f"  Visited: '{current}' | Current Queue: {list(queue)}")

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print("-" * 40)
    print(f"\nFinal BFS Traversal Order:")
    print(f"  {' -> '.join(traversal_order)}")
    print("=" * 60)

    return traversal_order

def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    bfs_traversal(graph, start_node='A')

if __name__ == "__main__":
    main()
