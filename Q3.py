from collections import deque

cap1 = 5
cap2 = 3
target = 4

queue = deque([(0, 0)])
visited = {(0, 0)}
found = False

while queue:
    curr = queue.popleft()
    j1, j2 = curr
    print(f"Visited state: ({j1}, {j2})")
    
    if j1 == target or j2 == target:
        print("Target Reached!")
        found = True
        break
        
    next_states = [
        (cap1, j2),
        (j1, cap2),
        (0, j2),
        (j1, 0),
        (j1 - min(j1, cap2 - j2), j2 + min(j1, cap2 - j2)),
        (j1 + min(j2, cap1 - j1), j2 - min(j2, cap1 - j1))
    ]
    
    for state in next_states:
        if state not in visited:
            visited.add(state)
            queue.append(state)

if not found:
    print("No Solution.")
