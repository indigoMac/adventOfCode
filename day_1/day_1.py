with open('input.txt', 'r') as file:
    # Read and process the file in one step
    pairs = [tuple(map(int, line.split())) for line in file]

# Separate and sort the numbers
list1, list2 = zip(*pairs)
list1, list2 = sorted(list1), sorted(list2)

total = sum(abs(a - b) for a, b in zip(list1, list2))

print(total)

similarity = sum(i * list2.count(i) for i in list1)
print(similarity)