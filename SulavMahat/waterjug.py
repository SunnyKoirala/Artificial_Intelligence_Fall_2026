from collections import deque

def water_jug(jug1, jug2, target):
    visited = set()
    queue = deque()
    
    # Initial state
    queue.append((0, 0))
    
    while queue:
        a, b = queue.popleft()
        
        # Skip if already visited
        if (a, b) in visited:
            continue
        visited.add((a, b))
        print(a, b)
        
        # Check if target is reached
        if a == target or b == target:
            print("Target found")
            return
        
        # Possible operations
        next_states = [
            (jug1, b),  # Fill jug1
            (a, jug2),  # Fill jug2
            (0, b),     # Empty jug1
            (a, 0),     # Empty jug2
            
            # Pour jug1 -> jug2
            (a - min(a, jug2 - b), b + min(a, jug2 - b)),
            
            # Pour jug2 -> jug1
            (a + min(b, jug1 - a), b - min(b, jug1 - a))
        ]
        
        for state in next_states:
            if state not in visited:
                queue.append(state)
    
    print("No solution")

# Driver Code
water_jug(5, 3, 4)