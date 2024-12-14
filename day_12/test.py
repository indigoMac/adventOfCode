import timeit
from collections import defaultdict

orth = [[0,1],[1,0],[0,-1],[-1,0]]

def rec(start, garden, region, visited): 
    plot = garden[start[0]][start[1]]
    for o in orth:
        next = tuple([sum(x) for x in zip(start, o)]) 
        if next[0] not in range(len(garden)) or next[1] not in range(len(garden[0])):
            continue
        if next not in visited and garden[next[0]][next[1]] == plot:
            visited.append(next)
            region.append(next)
            rec(next, garden, region, visited)

def find_regions(garden):
    regions = defaultdict(list)
    visited = []
    for i,r in enumerate(garden):
        for j,p in enumerate(r):
            if (i,j) in visited:
                continue
            region = [(i,j)]
            visited.append((i,j))
            rec((i,j), garden, region, visited)
            regions[p].append(region)
    return regions

def find_perimeter(region):
    perimeter = 0
    for p in region:
        for o in orth:
            if tuple([sum(x) for x in zip(p, o)]) not in region:
                perimeter += 1
    return perimeter

def find_perimeter_discount(region):
    print(region)
    sides = []
    for p in region:
        for i,o in enumerate(orth):
            next = tuple([sum(x) for x in zip(p, o)])  
            if next not in region:
                    sides.append((p, o))
    i=0
    sides_og = sides.copy()
    while i in range(len(sides)):
        side = sides[i]
        s,o = side
        o2 = orth[(orth.index(o)+1)%4]
        next = tuple([sum(x) for x in zip(s, o2)])
        while next in region and (next,o) in sides:
            if (next,o) in sides_og:
                sides.remove((next,o))
                i=0
            next = tuple([sum(x) for x in zip(next, o2)])
        i+=1
    print(len(sides))
    return len(sides)

def part1(input_file):
    garden = [list(x) for x in input_file.strip("\n\n").split("\n")]
    regions = find_regions(garden)
    solution = 0
    for r,v in regions.items():
        for i in v:
            per = find_perimeter(i)
            #print("{} {}".format(r, per))
            solution += len(i)*per
    return solution

def part2(input_file):
    garden = [list(x) for x in input_file.strip("\n\n").split("\n")]
    regions = find_regions(garden)
    solution = 0
    for r,v in regions.items():
        for i in v:
            per = find_perimeter_discount(i)
            #print("{} {}".format(r, per))
            solution += len(i)*per
    return solution

def solution():
    input_file = open("day_12/input copy.txt", "r").read()
    print(part1(input_file))
    print(part2(input_file))
    
def performance():
    my_setup = '''
from aoc import part1, part2
input_file = open("input.txt", "r").read()
'''
    print("Time for part1: {} sec".format(timeit.timeit(setup=my_setup, stmt='part1(input_file)', number = 1)))
    print("Time for part2: {} sec".format(timeit.timeit(setup=my_setup, stmt='part2(input_file)', number = 1)))

if __name__ == "__main__":
    solution()
    #performance()