import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(node, grid):
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        new_x, new_y = node[0] + dx, node[1] + dy
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 0:
            neighbors.append((new_x, new_y))
    return neighbors

def a_star(grid, start, goal):
    queue = []
    heapq.heappush(queue, (0 + heuristic(start, goal), 0, start, []))
    visited = set()
    
    while queue:
        _, cost, current, path = heapq.heappop(queue)
        if current == goal:
            return path + [current]
        
        visited.add(current)
        
        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                new_cost = cost + 1
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(queue, (priority, new_cost, neighbor, path + [current]))
    
    return None

grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

path = a_star(grid, start, goal)
if path:
    for step in path:
        print(step)
else:
    print("No path found.")
