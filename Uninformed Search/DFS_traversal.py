graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}


def dfs(start):

    stack = [start]

    visited = set()

    print("DFS Traversal:")

    while stack:

        node = stack.pop()

        if node not in visited:

            visited.add(node)

            print(node, end=" ")

            # Reverse so left-side node is visited first
            for neighbor in reversed(graph[node]):

                if neighbor not in visited:
                    stack.append(neighbor)


dfs('A')