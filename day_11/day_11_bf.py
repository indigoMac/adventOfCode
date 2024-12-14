from collections import Counter

def extract_data(file):
    with open(f"day_11/{file}.txt", 'r') as file:
        return file.read().strip('\n').split(' ')

def blink(stones):
    next_stones = Counter()
    for stone, count in stones.items():
        stone = str(stone)
        if stone == '0':
            next_stones['1'] += count
        elif len(stone) % 2 == 0:
            mid = len(stone) // 2
            next_stones[stone[:mid]] += count
            next_stones[str(int(stone[mid:]))] += count
        else:
            next_stones[str(int(stone) * 2024)] += count
    return next_stones

def count_stones(initial_stones, num_of_blinks):
    stones = Counter(initial_stones)
    for _ in range(num_of_blinks):
        stones = blink(stones)
    return sum(stones.values())

def main(num_of_blinks):
    stones = extract_data('input')  
    initial_stones = Counter(stones)  
    total_stones = count_stones(initial_stones, num_of_blinks)
    print(total_stones)

if __name__ == '__main__':
    num_of_blinks = 25
    main(num_of_blinks)
