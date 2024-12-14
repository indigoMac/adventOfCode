def is_safe(levels):
    """Check if a report is safe."""
    is_increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    valid_differences = all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))
    return (is_increasing or is_decreasing) and valid_differences

with open("input.txt", 'r') as file:
    reports = [tuple(map(int, line.split())) for line in file]

safe_count = 0

for levels in reports:

    if is_safe(levels):
        # Check if all differences are between 1 and 3
        safe_count += 1
    else:
        for i in range(len(levels)):
            modified_levels = levels[:i] + levels[i + 1:]
            if is_safe(modified_levels):
                safe_count += 1
                break

print(safe_count)
