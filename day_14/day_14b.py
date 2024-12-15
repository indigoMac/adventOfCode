import numpy as np
import re
from statistics import stdev
from itertools import pairwise
from copy import deepcopy

class Robot:
    def __init__(self, x, y, vx, vy):
        self.position = [x, y]
        self.velocity = [vx, vy]

    def move(self, time):
        self.position[0] += self.velocity[0] * time
        self.position[1] += self.velocity[1] * time

    def current_position(self, grid_width, grid_height):
        # Wrap around the grid
        return self.position[0] % grid_width, self.position[1] % grid_height

def extract_data(file):
    robots = []
    pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
    with open(file, "r") as f:
        for line in f:
            match = re.match(pattern, line.strip())
            if match:
                px, py, vx, vy = map(int, match.groups())
                robots.append(Robot(px, py, vx, vy))
    return robots

def simulate(robots, grid_width, grid_height, time):
    for robot in robots:
        robot.move(time)
    return [[robot.current_position(grid_width, grid_height) for robot in robots]]

def get_safety_factor(robots, grid_width, grid_height):
    quadrants = [0, 0, 0, 0]
    mid_x, mid_y = grid_width // 2, grid_height // 2

    for x, y in [robot.current_position(grid_width, grid_height) for robot in robots]:
        if x < mid_x and y < mid_y:
            quadrants[0] += 1  # Top-left
        elif x < mid_x and y >= mid_y:
            quadrants[1] += 1  # Bottom-left
        elif x >= mid_x and y >= mid_y:
            quadrants[2] += 1  # Bottom-right
        elif x >= mid_x and y < mid_y:
            quadrants[3] += 1  # Top-right

    return np.prod(quadrants)

def dist_stdev(nums):
    nums.sort()
    distances = [abs(a - b) for a, b in pairwise(nums)]
    return stdev(distances)

def get_order_score(robots, grid_width, grid_height):
    x_positions = [robot.current_position(grid_width, grid_height)[0] for robot in robots]
    y_positions = [robot.current_position(grid_width, grid_height)[1] for robot in robots]
    return dist_stdev(x_positions) + dist_stdev(y_positions)

def find_optimal_time(robots, grid_width, grid_height, max_time):
    max_order_score = 0
    best_time = 0
    for time in range(1, max_time + 1):
        simulate(robots, grid_width, grid_height, 1)
        order_score = get_order_score(robots, grid_width, grid_height)
        if order_score > max_order_score:
            max_order_score = order_score
            best_time = time
    return best_time

def draw(robots, grid_width, grid_height):
    grid = [[" " for _ in range(grid_width)] for _ in range(grid_height)]
    for x, y in [robot.current_position(grid_width, grid_height) for robot in robots]:
        grid[y][x] = "#"
    for row in grid:
        print("".join(row))

def main():
    file = "day_14/input.txt"
    grid_width, grid_height = 101, 103
    robots = extract_data(file)

    # Solve Part 1
    simulate(robots, grid_width, grid_height, 100)
    safety_factor = get_safety_factor(robots, grid_width, grid_height)
    print("Part 1 Safety Factor:", safety_factor)

    # Solve Part 2
    robots = extract_data(file)  # Reset robots
    best_time = find_optimal_time(robots, grid_width, grid_height, max_time=10000)
    print("Part 2 Optimal Time:", best_time)

    # Visualize the pattern at the best time
    robots = extract_data(file)  # Reset robots
    simulate(robots, grid_width, grid_height, best_time)
    draw(robots, grid_width, grid_height)

if __name__ == "__main__":
    main()
