def dfs_traversal(graph, start_node='A'):
    print("=" * 60)
    print("QUESTION 7: DEPTH FIRST SEARCH (DFS) TRAVERSAL (USING STACK)")
    print("=" * 60)
    print(f"Start Node: {start_node}\n")

    stack = [start_node]
    visited = set()
    traversal_order = []

    print("DFS Traversal Steps:")
    print("-" * 40)

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.add(current)
            traversal_order.append(current)
            print(f"  Visited: '{current}' | Current Stack: {stack}")

            for neighbor in reversed(graph.get(current, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    print("-" * 40)
    print(f"\nFinal DFS Traversal Order:")
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

    dfs_traversal(graph, start_node='A')

if __name__ == "__main__":
    main()
