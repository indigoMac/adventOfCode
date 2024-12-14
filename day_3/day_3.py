import re

# Read the corrupted memory data from the file
with open('input.txt', 'r') as file:
    data = file.read()

# Find positions of all "do" and "don't" markers
marker_pattern = r"\b(do|don't)\b"
markers = [(match.group(0), match.start()) for match in re.finditer(marker_pattern, data)]

# Sort markers by their positions in the text
# markers.sort(key=lambda x: x[1])

# Determine ranges to exclude
exclusion_ranges = []
i = 0
while i < len(markers):
    if markers[i][0] == "don't":
        # Find the next "do" after this "don't"
        start = markers[i][1]
        end = None
        for j in range(i + 1, len(markers)):
            if markers[j][0] == "do":
                end = markers[j][1]
                i = j  # Skip to the "do" marker
                break
        if end is None:
            # No "do" found, exclude until the end of the data
            end = len(data)
        exclusion_ranges.append((start, end))
    i += 1

# Remove excluded ranges from the data
cleaned_data = []
prev_end = 0
for start, end in exclusion_ranges:
    cleaned_data.append(data[prev_end:start])  # Add valid data before this range
    prev_end = end
cleaned_data.append(data[prev_end:])  # Add remaining valid data
cleaned_data = ''.join(cleaned_data)

# Extract valid `mul(X,Y)` instructions from cleaned data
mul_pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(mul_pattern, cleaned_data)

# Compute the sum of results
total = sum(int(x) * int(y) for x, y in matches)

print(total)
