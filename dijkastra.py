from collections import deque
import heapq
import matplotlib.pyplot as plt
import numpy as np


def dijkstra(grid):
    n = len(grid)
    m = len(grid[0])
    goal = (n - 1, m - 1)
    pq = []
    heapq.heappush(pq, (0, 0, 0, [(0, 0)]))  # cost, x, y, path
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        cost, x, y, path = heapq.heappop(pq)
        if (x, y) == goal:
            return path, cost

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                new_cost = cost + 1  # assuming uniform cost of 1
                heapq.heappush(pq, (new_cost, nx, ny, path + [(nx, ny)]))
    return None, None

# Test the algorithm

grid = [
[0,0,0,0,0,0,1,0,0,0],
[1,1,1,1,1,0,1,0,1,0],
[0,0,0,0,1,0,1,0,1,0],
[0,1,1,0,1,0,1,0,1,0],
[0,1,0,0,0,0,1,0,1,0],
[0,1,0,1,1,1,1,0,1,0],
[0,1,0,0,0,0,0,0,1,0],
[0,1,1,1,1,1,1,0,1,0],
[0,0,0,0,0,0,0,0,1,0],
[1,1,1,1,1,1,1,0,0,0]
]

print("\nDijkstra's:")
dijkstra_path, dijkstra_length = dijkstra(grid)
if dijkstra_path:
    print("Path:", dijkstra_path)
    print("Length:", dijkstra_length)
else:
    print("No path found")


def dfs(grid, x, y, goal, visited, path, all_paths):
    n = len(grid)
    m = len(grid[0])
    if (x, y) == goal:
        all_paths.append(path.copy())
        return

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                path.append((nx, ny))
                dfs(grid, nx, ny, goal, visited, path, all_paths)
                path.pop()
                visited[nx][ny] = False    

def plot_path(grid, path, title, color):
    n = len(grid)
    m = len(grid[0])
    grid_array = np.array(grid)
    
    plt.figure(figsize=(6, 6))
    plt.imshow(grid_array, cmap='Greys', origin='upper')
    
    if path:
        path_x = [p[1] for p in path]
        path_y = [p[0] for p in path]
        plt.plot(path_x, path_y, color=color, linewidth=3, marker='o', markersize=8)
    
    plt.title(title)
    plt.xticks(range(m))
    plt.yticks(range(n))
    plt.grid(True, which='both', color='black', linewidth=1)
    plt.show()


    plot_path(grid, dijkstra_path, "Dijkstra's Path", 'purple')