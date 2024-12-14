from itertools import product

def parse_input(filename):
    """
    Parse the input file to extract test values and corresponding numbers.
    """
    equations = []
    with open(filename, "r") as file:
        for line in file:
            test_value, numbers = line.strip().split(": ")
            test_value = int(test_value)
            numbers = list(map(int, numbers.split()))
            equations.append((test_value, numbers))
    return equations


def evaluate_left_to_right(numbers, operators):
    """
    Evaluate an expression given numbers and operators, left-to-right.
    """
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result


def can_match_target(target, numbers):
    """
    Check if the target can be achieved by any combination of operators.
    """
    # Generate all combinations of `+` and `*` for the `n-1` operator positions
    num_operators = len(numbers) - 1
    ops = ['+', '*', '||']
    for operators in product(ops, repeat=num_operators):
        if evaluate_left_to_right(numbers, operators) == target:
            return True  # A matching combination is found
    return False


def calculate_calibration(filename):
    """
    Calculate the total calibration result by summing valid test values.
    """
    equations = parse_input(filename)
    total = 0

    for test_value, numbers in equations:
        if can_match_target(test_value, numbers):
            total += test_value

    return total


if __name__ == "__main__":
    # Replace 'input.txt' with the actual input file
    total_calibration = calculate_calibration("day_7/input.txt")
    print(f"Total Calibration Result: {total_calibration}")
