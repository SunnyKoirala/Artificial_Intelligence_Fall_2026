from collections import deque

def solve_water_jug_bfs(cap1=5, cap2=3, target=4):
    print("=" * 60)
    print("QUESTION 3: WATER JUG PROBLEM USING BFS")
    print("=" * 60)
    print(f"Configurations:")
    print(f"  - Jug 1 Capacity: {cap1}L")
    print(f"  - Jug 2 Capacity: {cap2}L")
    print(f"  - Target Amount:  {target}L\n")

    start_state = (0, 0)

    queue = deque([(start_state, [start_state])])

    visited = set()
    visited.add(start_state)

    visited_order = []
    solution_path = None

    print("Visited States during Exploration:")
    print("-" * 40)

    while queue:
        current_state, path = queue.popleft()
        j1, j2 = current_state
        visited_order.append(current_state)
        print(f"  Visited State #{len(visited_order)}: Jug 1 = {j1}L, Jug 2 = {j2}L")

        if j1 == target or j2 == target:
            solution_path = path
            break

        next_states = []

        next_states.append((cap1, j2))
        next_states.append((j1, cap2))
        next_states.append((0, j2))
        next_states.append((j1, 0))
        pour_1_to_2 = min(j1, cap2 - j2)
        next_states.append((j1 - pour_1_to_2, j2 + pour_1_to_2))
        pour_2_to_1 = min(j2, cap1 - j1)
        next_states.append((j1 + pour_2_to_1, j2 - pour_2_to_1))

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

    print("-" * 40)
    
    if solution_path:
        print("\nSolution Found! Path to Target:")
        for step, (j1, j2) in enumerate(solution_path):
            print(f"  Step {step}: Jug 1 = {j1}L, Jug 2 = {j2}L")
    else:
        print("\nNo Solution.")
    
    print("=" * 60)

if __name__ == "__main__":
    solve_water_jug_bfs()
