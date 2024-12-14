import numpy as np
from collections import deque, defaultdict

def extract_data(file):
    with open(f'day_12/{file}.txt', 'r') as file:
        return np.array([list(line.strip()) for line in file])

def find_key_coordinates(garden):
    key_coordinates = {}
    rows, cols = garden.shape

    for x in range(rows):
        for y in range(cols):
            plant = garden[x][y]
            key_coordinates.setdefault(plant, []).append((x, y))
            
    return key_coordinates

def find_plots(coordinates):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()
    groups = []

    def bfs(start):
        """Perform BFS to find all connected neighbors."""
        queue = deque([start])
        group = []

        while queue:
            x, y = queue.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            group.append((x, y))

            # Check all neighbors
            for dx, dy in directions:
                neighbor = (x + dx, y + dy)
                if neighbor in coordinates and neighbor not in visited:
                    queue.append(neighbor)

        return group
    
    for coord in coordinates:
        if coord not in visited:
            group = bfs(coord)
            groups.append(group)

    return groups

def get_fence_price(garden, groups):
    rows, cols = garden.shape
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    cost = 0

    for group in groups:
        area = len(group)
        fences = 0
        for x, y in group:
            # Calculate neighbors
            num_neighbours = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if garden[nx, ny] == garden[x, y]:
                        num_neighbours += 1
            # Add fences for the cell
            fences += (4 - num_neighbours)
        # Add the cost for the group
        cost += fences * area
    return cost

#### or this also works ###
# def get_fence_price(garden, groups):
#     rows, cols = garden.shape
#     directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#     cost = 0

#     for group in groups:
#         area = len(group)
#         edges = 0

#         for x, y in group:
#             # Calculate edges for the cell
#             for dx, dy in directions:
#                 nx, ny = x + dx, y + dy
#                 # An edge exists if it's out of bounds or a different plant
#                 if not (0 <= nx < rows and 0 <= ny < cols) or garden[nx, ny] != garden[x, y]:
#                     edges += 1

#         # Cost is area multiplied by total edges
#         cost += area * edges

def main():
    garden = extract_data('input copy') 
    print("Garden:")
    print(garden)

    key_coordinates = find_key_coordinates(garden)
    print("\nKey Coordinates:")
    print(key_coordinates)

    plots = {}
    for key, value in key_coordinates.items():
        plots[key] = find_plots(value)

    total_price = 0
    print("\nPlots:")
    for plant, groups in plots.items():
        print(f"{plant}: {groups}")
        total_price += get_fence_price(garden, groups)
    print("\nTotal Fencing Price:", total_price)

if __name__ == '__main__':
    main()
