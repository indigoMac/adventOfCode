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

def find_perimeter_discount(region):
    sides = []
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    for p in region:
        for i,o in enumerate(directions):
            next = tuple([sum(x) for x in zip(p, o)])  
            if next not in region:
                    sides.append((p, o))
    i=0
    sides_og = sides.copy()
    while i in range(len(sides)):
        side = sides[i]
        s,o = side
        o2 = directions[(directions.index(o)+1)%4]
        next = tuple([sum(x) for x in zip(s, o2)])
        while next in region and (next,o) in sides:
            if (next,o) in sides_og:
                sides.remove((next,o))
                i=0
            next = tuple([sum(x) for x in zip(next, o2)])
        i+=1
    return len(sides)

def get_fence_price(groups):

    cost = 0
    for group in groups:
        area = len(group)
        fences = find_perimeter_discount(group)
        
        cost += fences * area
    return cost

def main():
    garden = extract_data('input') 
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
        # print(f"{plant}: {groups}")
        total_price += get_fence_price(groups)
    print("\nTotal Fencing Price:", total_price)

if __name__ == '__main__':
    main()
