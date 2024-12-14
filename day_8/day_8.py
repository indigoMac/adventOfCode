import numpy as np
from collections import defaultdict
import itertools

def extract_data(filename):
    with open(f"day_8/{filename}.txt", "r") as file:
        lines = [list(line) for line in file.read().splitlines()]
        return np.array(lines)
    
def find_antenas(map):
    antena_locations = defaultdict(list)
    for (row, col), value in np.ndenumerate(map):
        if value != '.':
            antena_locations[value].append((row,col))
    antena_locations = dict(antena_locations)
    return antena_locations

def find_antinodes(char, locations):
    antinodes = set()
    if len(locations) < 2:
        return antinodes
    
    locations = sorted(locations)
    
    for(x1,y1), (x2,y2) in itertools.combinations(locations, 2):
        dx, dy = x2 - x1, y2 - y1
        
        new_x, new_y = x2 + dx, y2 + dy
        antinodes.add((new_x, new_y))
        
        new_x, new_y = x1 - dx, y1 - dy
        antinodes.add((new_x, new_y))
    return antinodes
        
if __name__ == '__main__':
    map = extract_data('input')
    print(map)
    antena_locations = find_antenas(map)
    print(antena_locations)
    
    all_antinodes = {}
    count = 0
    for char, locations in antena_locations.items():
        new_antenas = find_antinodes(char, locations)
        count += len(new_antenas)
        all_antinodes[char] = new_antenas

    print(count)
    
    max_row = max(p[0] for locs in antena_locations.values() for p in locs)
    max_col = max(p[1] for locs in antena_locations.values() for p in locs)

    for points in all_antinodes.values():
        for x, y in points:
            max_row = max(max_row, x)
            max_col = max(max_col, y)

    # Create an expanded array to accommodate new points
    new_array = map.copy() #np.full((max_row + 1, max_col + 1), '.', dtype=str)

    # Copy original array
    for (row, col), value in np.ndenumerate(map):
        new_array[row, col] = value

    # Add new points
    for char, points in all_antinodes.items():
        for x, y in points:
            if 0 <= x < new_array.shape[0] and 0 <= y < new_array.shape[1]:
                new_array[x, y] = '#'

    print(new_array)
    
    print(np.sum(new_array == '#'))