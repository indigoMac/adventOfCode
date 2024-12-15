import numpy as np
import re

class Robot:
    def __init__(self, x, y, vx, vy):
        self.starting_point = (x , y)
        self.velocity = (vx, vy)
    
    def start(self):
        return int(self.starting_point[0]), int(self.starting_point[1])
    
    def move(self, time, grid_width, grid_height):
        new_x = (self.starting_point[0] + self.velocity[0] * time) % grid_width
        new_y = (self.starting_point[1] + self.velocity[1] * time) % grid_height
        return int(new_x), int(new_y)
        

def extract_data(file):
    robots = []
    
    pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
    
    with open(f"day_14/{file}.txt", "r") as file:
        for line in file:
            match = re.match(pattern, line.strip('\n'))
            
            if match:
                px, py, vx, vy = map(int, match.groups())
                robots.append({
                "position": (px, py),
                "velocity": (vx, vy)
                })
    return robots

def split_grid(grid):
    grid_height, grid_width = grid.shape
    mid_x = grid_width // 2
    mid_y = grid_height // 2
    
    # Extract quadrants
    top_left = grid[:mid_y, :mid_x]
    top_right = grid[:mid_y, mid_x+1:]
    bottom_left = grid[mid_y+1:, :mid_x]
    bottom_right = grid[mid_y+1:, mid_x+1:]
    
    return top_left, top_right, bottom_left, bottom_right

def count_robots(quadrants):
    counts = [int(np.sum(quad)) for quad in quadrants]
    return counts


def main(practice = False):
    if practice == True:
        robots = extract_data("input copy")
        grid = np.zeros((7,11))
    else:
        robots = extract_data("input")
        grid = np.zeros((103,101))
    
    grid_height ,grid_width = grid.shape
    start_grid = grid.copy()
    
    for robot in robots:
        bot = Robot(robot['position'][0],robot['position'][1],
                    robot['velocity'][0],robot['velocity'][1])
        
        new_x, new_y = bot.start()
        start_grid[new_y][new_x] += 1
        
        new_x, new_y = bot.move(100, grid_width, grid_height)
        grid[new_y][new_x] += 1
    
    quadrants = split_grid(grid)
    counts = count_robots(quadrants)
    safety_factor = np.prod(counts)
    print(safety_factor)
    
if __name__ == '__main__':
    main(practice = False)