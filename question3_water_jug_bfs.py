from collections import deque

# Capacities
JUG1 = 5
JUG2 = 3
TARGET = 4


def get_next_states(state):
    x, y = state

    states = []

    # 1. Fill Jug 1
    states.append((JUG1, y))

    # 2. Fill Jug 2
    states.append((x, JUG2))

    # 3. Empty Jug 1
    states.append((0, y))

    # 4. Empty Jug 2
    states.append((x, 0))

    # 5. Pour Jug 1 -> Jug 2
    amount = min(x, JUG2 - y)
    states.append((x - amount, y + amount))

    # 6. Pour Jug 2 -> Jug 1
    amount = min(y, JUG1 - x)
    states.append((x + amount, y - amount))

    return states


def water_jug_bfs():

    queue = deque()

    # Starting state
    start = (0, 0)

    queue.append(start)

    # Visited states
    visited = set()
    visited.add(start)

    while queue:

        current = queue.popleft()

        # Print every visited state
        print("Visited:", current)

        x, y = current

        # Check target
        if x == TARGET or y == TARGET:
            print("\nTarget found:", current)
            return

        # Generate next states
        for next_state in get_next_states(current):

            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)

    print("No Solution.")


# Run BFS
water_jug_bfs()