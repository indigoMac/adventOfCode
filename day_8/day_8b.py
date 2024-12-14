import numpy as np
from collections import defaultdict
import itertools


def extract_map(filename):
    """
    Reads the map data from a file and returns it as a NumPy array.
    """
    with open(f"day_8/{filename}.txt", "r") as file:
        lines = [list(line) for line in file.read().splitlines()]
        return np.array(lines)


def find_antennas(map_array):
    """
    Finds the locations of all antennas in the map and groups them by their frequencies.
    """
    antenna_locations = defaultdict(list)
    for (row, col), value in np.ndenumerate(map_array):
        if value != '.':  # Ignore empty cells
            antenna_locations[value].append((row, col))
    return dict(antenna_locations)


def find_antinodes(frequency, locations, map_array):
    """
    Finds all antinodes for a given frequency and its antenna locations.
    """
    antinodes = set()
    rows, columns = map_array.shape

    # Skip if there are fewer than 2 antennas for the frequency
    if len(locations) < 2:
        return antinodes

    # Sort locations for consistency
    locations = sorted(locations)

    # Check all pairs of antennas for alignment
    for (x1, y1), (x2, y2) in itertools.combinations(locations, 2):
        dx, dy = x2 - x1, y2 - y1

        # Extend in the positive direction
        new_x, new_y = x2 + dx, y2 + dy
        while 0 <= new_x < rows and 0 <= new_y < columns:
            antinodes.add((new_x, new_y))
            new_x, new_y = new_x + dx, new_y + dy

        # Extend in the negative direction
        new_x, new_y = x1 - dx, y1 - dy
        while 0 <= new_x < rows and 0 <= new_y < columns:
            antinodes.add((new_x, new_y))
            new_x, new_y = new_x - dx, new_y - dy

    return antinodes


def add_antinodes_to_map(map_array, antinodes):
    """
    Adds antinodes to the map array, ensuring no overlap with existing antennas.
    """
    # Create a copy of the original map
    updated_map = map_array.copy()

    # Add antinodes to the map
    for char, points in antinodes.items():
        for x, y in points:
            if updated_map[x, y] == '.':  # Only add if the cell is empty
                updated_map[x, y] = '#'

    return updated_map


def count_total_antinodes(map_array):
    """
    Counts the total number of antinodes in the map (non-empty cells).
    """
    return np.sum(map_array != '.')


if __name__ == '__main__':
    # Load map data
    map_data = extract_map('input')
    print("Original Map:")
    print(map_data)

    # Find antennas by frequency
    antenna_locations = find_antennas(map_data)
    print("\nAntenna Locations:")
    print(antenna_locations)

    # Calculate antinodes for each frequency
    all_antinodes = {}
    for frequency, locations in antenna_locations.items():
        all_antinodes[frequency] = find_antinodes(frequency, locations, map_data)

    # Count all unique antinodes
    total_antinodes = sum(len(points) for points in all_antinodes.values())
    print(f"\nTotal unique antinodes: {total_antinodes}")

    # Update the map with antinodes
    updated_map = add_antinodes_to_map(map_data, all_antinodes)
    print("\nUpdated Map with Antinodes:")
    print(updated_map)

    # Count the total impact
    impact = count_total_antinodes(updated_map)
    print(f"\nTotal Impact (Unique Locations with Antinodes): {impact}")
