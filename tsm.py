import numpy as np
def nearest_neighbor(graph, start):
    num_cities = len(graph)
    visited = [False] * num_cities
    path = [start]
    visited[start] = True
    
    for _ in range(num_cities - 1):
        current_city = path[-1]
        nearest_city = None
        nearest_distance = float('inf')
        for city in range(num_cities):
            if not visited[city] and graph[current_city][city] < nearest_distance:
                nearest_city = city
                nearest_distance = graph[current_city][city]
        path.append(nearest_city)
        visited[nearest_city] = True
    
    path.append(start)  # Return to the start city
    return path
graph = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])
start_city = 0
shortest_path = nearest_neighbor(graph, start_city)
print("Shortest path:", shortest_path)