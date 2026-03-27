# With BFS

from collections import deque

def bfs():
    queue = deque([(0, 0)])
    visited = set()

    while queue:
        a, b = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        print((a, b))

        if b == 2:
            print("Goal reached:", (a, b))
            return

        states = [
            (3, b),   # Fill jug A
            (a, 4),   # Fill jug B
            (0, b),   # Empty jug A
            (a, 0),   # Empty jug B
            (max(0, a - (4 - b)), min(4, b + a)),  # Pour A → B
            (min(3, a + b), max(0, b - (3 - a)))   # Pour B → A
        ]

        for s in states:
            if s not in visited:
                queue.append(s)

bfs()