import numpy as np

def extract_map():
    with open('day_6/input.txt', 'r') as file:
        data = file.read()
        lines = [list(line) for line in data.splitlines()]
        return np.array(lines)


def isValid(x, y, sizeX, sizeY):
    """
    Check if the given coordinate is within the map bounds.
    """
    return 0 <= x < sizeX and 0 <= y < sizeY

def find_starting_position(map):
    coordinates = np.where(map == '^')
    return coordinates[0][0], coordinates[1][0]

def find_route(map, start_x, start_y):
    rows, cols = map.shape

    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    facing = 0  # Initial direction is "up"

    x, y = start_x, start_y
    
    visited = set()
    visited.add((x, y))

    while isValid(x, y, rows, cols):
        dx, dy = directions[facing]

        # Check the next position
        nx, ny = x + dx, y + dy
        if isValid(nx, ny, rows, cols) and map[nx, ny] != '#':
            # Move to the next position
            x, y = nx, ny
            visited.add((x, y))
        elif isValid(nx, ny, rows, cols) and map[nx, ny] == '#':
            # Turn right (update facing direction)
            facing = (facing + 1) % 4
        else: 
            break
    return len(visited)

if __name__ == "__main__":
    map = extract_map()
    startX, startY = find_starting_position(map)
    print(startX, startY)
    num_positions = find_route(map, startX, startY)
    print(num_positions)