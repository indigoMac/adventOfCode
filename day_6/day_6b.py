import numpy as np


def extract_map(filename="day_6/input.txt"):
    """
    Read the map from the input file and convert it to a NumPy array.
    """
    with open(filename, 'r') as file:
        lines = [list(line.strip()) for line in file]
    return np.array(lines)


def is_valid(x, y, rows, cols):
    """
    Check if the given position (x, y) is within the bounds of the map.
    """
    return 0 <= x < rows and 0 <= y < cols


def find_starting_position(map):
    """
    Find the starting position of the guard (marked as ^) in the map.
    """
    coordinates = np.where(map == '^')
    return coordinates[0][0], coordinates[1][0]


def simulate_route(map, start_x, start_y, detect_loop=False):
    """
    Simulate the guard's patrol route and optionally detect loops.
    
    Parameters:
    - map: The lab map as a NumPy array.
    - start_x, start_y: Starting coordinates of the guard.
    - detect_loop: If True, detect and return whether a loop occurs.
    
    Returns:
    - If detect_loop is False: A set of visited positions and direction map.
    - If detect_loop is True: True if a loop is detected, otherwise False.
    """
    rows, cols = map.shape

    # Directions: up, right, down, left
    directions = {
        0: (-1, 0),  # up
        1: (0, 1),   # right
        2: (1, 0),   # down
        3: (0, -1)   # left
    }

    x, y = start_x, start_y
    facing = 0  # Initial direction is "up"

    visited = set()
    visited_with_directions = set()

    while is_valid(x, y, rows, cols):
        current_state = ((x, y), facing)

        if detect_loop and current_state in visited_with_directions:
            return True  # Loop detected

        if not detect_loop:
            visited.add((x, y))

        visited_with_directions.add(current_state)

        dx, dy = directions[facing]
        nx, ny = x + dx, y + dy

        if is_valid(nx, ny, rows, cols) and map[nx, ny] != '#':
            x, y = nx, ny
        elif is_valid(nx, ny, rows, cols) and map[nx, ny] == '#':
            facing = (facing + 1) % 4  # Turn right
        else:
            break

    return visited if not detect_loop else False


def add_obstruction(map, start_x, start_y, route):
    """
    Find all valid positions where adding an obstruction creates a loop.
    """
    valid_positions = []

    for position in route:
        if position == (start_x, start_y):
            continue  # Skip the starting position

        modified_map = map.copy()
        modified_map[position[0], position[1]] = '#'

        if simulate_route(modified_map, start_x, start_y, detect_loop=True):
            valid_positions.append(position)

    return valid_positions


if __name__ == "__main__":
    # Load the map and find the starting position
    map = extract_map()
    start_x, start_y = find_starting_position(map)

    # Find the initial route of the guard
    route = simulate_route(map, start_x, start_y)

    # Find valid obstruction positions
    valid_positions = add_obstruction(map, start_x, start_y, route)

    # Output results
    print(f"Valid obstruction positions: {valid_positions}")
    print(f"Number of valid positions: {len(valid_positions)}")
