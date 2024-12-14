import re
from math import gcd
import sympy

def extract_data(file):
    machines = []

    button_pattern = r"Button ([AB]): X\+(\d+), Y\+(\d+)"
    prize_pattern = r"Prize: X=(\d+), Y=(\d+)"

    with open(f"day_13/{file}.txt") as file:
        machine = {}
        for line in file:
            if line == '\n':
                if machine:
                    machines.append(machine)
                    machine = {}
                continue
            
            button_match = re.match(button_pattern, line)
            if button_match:
                button, x, y = button_match.groups()
                machine[f'button_{button.lower()}'] = (int(x), int(y))
                continue

            prize_match = re.match(prize_pattern, line)
            if prize_match:
                x, y = prize_match.groups()
                machine['prize'] = (int(x), int(y))
            
        if machine:
            machines.append(machine)

        return machines

def find_minimum_presses(ax, ay, bx, by, tx, ty):
    """
    Finds the minimum number of presses to reach (tx, ty) using vectors (ax, ay) and (bx, by)
    using the derived formula:
        b = (py * ax - px * ay) / (by * ax - bx * ay)
        a = (px - b * bx) / ax
    """
    # Compute the denominator for b
    denominator = by * ax - bx * ay

    if denominator == 0:
        return None

    # Check if (py * ax - px * ay) is divisible by the denominator
    numerator_b = ty * ax - tx * ay
    if numerator_b % denominator != 0:
        return None

    # Calculate b
    b = numerator_b // denominator

    # Check if (px - b * bx) is divisible by ax
    numerator_a = tx - b * bx
    if numerator_a % ax != 0:
        return None

    # Calculate a
    a = numerator_a // ax

    # Ensure non-negative solutions
    if a < 0 or b < 0:
        return None

    # Return the results
    return a, b   

def solve(ax, ay, bx, by, tx, ty):
    a, b = sympy.symbols("a, b", integer=True)
    
    equations = [
        sympy.Eq(a*ax + b*bx, tx), 
        sympy.Eq(a*ay + b*by, ty)
    ]

    try:
        solution_list = []
        solutions = sympy.solve(equations, (a, b))
        
        if solutions:
            if isinstance(solutions, dict):
                solutions = [solutions]

            for solution in solutions:
                solution_list.append((solution[a], solution[b]))
        return solution_list
    except(sympy.SympifyError, IndexError) as e:
        return None



def cost(machine):
    solutions = solve(machine['button_a'][0],machine['button_a'][1],
                      machine['button_b'][0], machine['button_b'][1],
                      machine['prize'][0], machine['prize'][1] )

    if solutions:
        return min(((a * 3) + b) for (a, b) in solutions)
    return None

def main():
    claw_machines = extract_data('input')
    print(claw_machines)

    tokens = 0
    for machine in claw_machines:
        costs = cost(machine)

        if costs: 
            tokens += costs
    
    print(tokens)

if __name__ == '__main__':
    main()