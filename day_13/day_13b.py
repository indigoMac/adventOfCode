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
                      machine['prize'][0] + 10000000000000, machine['prize'][1] + 10000000000000 )

    if solutions:
        return min(((a * 3) + b) for (a, b) in solutions)
    return None

def main():
    claw_machines = extract_data('input')

    tokens = 0
    for machine in claw_machines:
        costs = cost(machine)

        if costs: 
            tokens += costs
    
    print(tokens)

if __name__ == '__main__':
    main()