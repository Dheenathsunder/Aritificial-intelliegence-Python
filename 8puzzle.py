from collections import deque

def print_board(board):
    for row in board:
        print(row)
    print()

def find_blank(board):
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == 0:
                return i, j

def get_neighbors(board):
    neighbors = []
    x, y = find_blank(board)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_board = [row[:] for row in board]
            new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
            neighbors.append(new_board)
    return neighbors

def solve_puzzle(start, goal):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        board, path = queue.popleft()
        visited.add(tuple(map(tuple, board)))

        if board == goal:
            return path + [board]

        for neighbor in get_neighbors(board):
            if tuple(map(tuple, neighbor)) not in visited:
                queue.append((neighbor, path + [board]))

    return None

start = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

solution = solve_puzzle(start, goal)
if solution:
    for step in solution:
        print_board(step)
else:
    print("No solution found.")
