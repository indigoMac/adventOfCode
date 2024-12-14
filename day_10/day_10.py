import numpy as np
from collections import deque

def extract_map(file):
    with open(f'day_10/{file}.txt', 'r') as file:
        lines = [list(line) for line in file.read().splitlines()]
        return np.array(lines).astype(int)

def find_positions(map, value):
    coordinates = np.argwhere(map == value)
    return coordinates.tolist()

def find_score_for_trailhead(grid, start):
    """Finds the score for a single trailhead using BFS."""
    rows, cols = grid.shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right
    queue = deque([start])
    visited = set()
    reachable_nines = set()

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        current_height = grid[x, y]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:  # Within bounds
                next_height = grid[nx, ny]
                if next_height == current_height + 1:  # Valid hiking trail step
                    if next_height == 9:
                        reachable_nines.add((nx, ny))
                    else:
                        queue.append((nx, ny))

    return len(reachable_nines)

def calculate_total_score(grid):
    """Calculates the total score for all trailheads."""
    trailheads = find_positions(grid, 0)
    total_score = 0

    for trailhead in trailheads:
        total_score += find_score_for_trailhead(grid, tuple(trailhead))

    return total_score

def main():
    map = extract_map('input')
    print(map)
    
    print(calculate_total_score(map))

if __name__ == '__main__':
    main()