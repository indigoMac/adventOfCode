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
        raise ValueError("The steps do not allow reaching the target.")

    # Check if (py * ax - px * ay) is divisible by the denominator
    numerator_b = ty * ax - tx * ay
    if numerator_b % denominator != 0:
        raise ValueError("Target coordinates cannot be reached with integer steps.")

    # Calculate b
    b = numerator_b // denominator

    # Check if (px - b * bx) is divisible by ax
    numerator_a = tx - b * bx
    if numerator_a % ax != 0:
        raise ValueError("Target coordinates cannot be reached with integer steps.")

    # Calculate a
    a = numerator_a // ax

    # Ensure non-negative solutions
    if a < 0 or b < 0:
        raise ValueError("Target coordinates cannot be reached with non-negative steps.")

    # Return the results
    return a, b, a + b

# Example usage:
button_a = (94, 34)
button_b = (22, 67)
target = (8400, 5400)

try:
    result = find_minimum_presses(*button_a, *button_b, *target)
    print("Minimum presses (a, b, total):", result)
except ValueError as e:
    print("Error:", e)
