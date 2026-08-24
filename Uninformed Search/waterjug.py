from collections import deque

jug1_capacity = 5
jug2_capacity = 3
target = 4


def water_jug_bfs():

    queue = deque()

    # Start state
    queue.append((0, 0))

    visited = set()

    while queue:

        current = queue.popleft()

        if current in visited:
            continue

        visited.add(current)

        x, y = current

        print("Visited:", current)

        # Check target
        if x == target or y == target:
            print("Target Found!")
            return

        # Generate possible states

        states = []

        # Fill Jug 1
        states.append((jug1_capacity, y))

        # Fill Jug 2
        states.append((x, jug2_capacity))

        # Empty Jug 1
        states.append((0, y))

        # Empty Jug 2
        states.append((x, 0))

        # Pour Jug 1 into Jug 2
        pour = min(x, jug2_capacity - y)

        states.append((
            x - pour,
            y + pour
        ))

        # Pour Jug 2 into Jug 1
        pour = min(y, jug1_capacity - x)

        states.append((
            x + pour,
            y - pour
        ))

        # Add unvisited states
        for state in states:

            if state not in visited:
                queue.append(state)

    print("No Solution")


water_jug_bfs()