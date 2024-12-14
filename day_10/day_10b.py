import numpy as np
from collections import deque

def extract_map(file):
    with open(f'day_10/{file}.txt', 'r') as file:
        lines = [list(line) for line in file.read().splitlines()]
        return np.array(lines).astype(int)

def find_positions(grid, value):
    """Find all positions in the grid with the specified value."""
    return np.argwhere(grid == value).tolist()

def find_trailhead_rating(grid, start):
    """Finds the trailhead rating (number of distinct hiking trails) using BFS."""
    rows, cols = grid.shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right
    queue = deque([(start, [])])  # Each element is (current position, current path)
    trails = set()

    while queue:
        (x, y), path = queue.popleft()
        print((x, y))
        print(path)
        # Append current position to the path
        new_path = path + [(x, y)]
        current_height = grid[x, y]

        # If we've reached height 9, save the trail
        if current_height == 9:
            trails.add(tuple(new_path))
            continue

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:  # Within bounds
                next_height = grid[nx, ny]
                if next_height == current_height + 1:  # Valid hiking trail step
                    queue.append(((nx, ny), new_path))

    return len(trails)

def calculate_total_rating(grid):
    """Calculates the total rating for all trailheads."""
    trailheads = find_positions(grid, 0)
    total_rating = 0

    for trailhead in trailheads:
        total_rating += find_trailhead_rating(grid, tuple(trailhead))

    return total_rating

def main():
    # Load the map
    topographic_map = extract_map('input copy')

    # Calculate the total trailhead rating
    total_rating = calculate_total_rating(topographic_map)

    print("Total Trailhead Rating:", total_rating)

if __name__ == '__main__':
    main()
