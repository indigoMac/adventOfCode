from collections import Counter

def extract_data(file):
    """
    Reads the stone data from the input file and returns it as a Counter.
    """
    with open(f"day_11/{file}.txt", 'r') as file:
        stones = file.read().strip('\n').split(' ')
        return Counter(stones)

def process_stone(stone, memo):
    """
    Processes a single stone and returns the resulting stones, using memoization.
    """
    if stone in memo:
        return memo[stone]

    stone = str(stone)
    if stone == '0':
        result = ['1']
    elif len(stone) % 2 == 0:
        mid = len(stone) // 2
        left, right = stone[:mid], str(int(stone[mid:]))
        result = [left, right]
    else:
        result = [str(int(stone) * 2024)]

    memo[stone] = result  # Cache the result
    return result

def blink(stones, memo):
    """
    Processes all stones for one blink, using memoization to avoid redundant calculations.
    """
    updated_stones = Counter()
    for stone, count in stones.items():
        for new_stone in process_stone(stone, memo):
            updated_stones[new_stone] += count
    return updated_stones

def count_stones_memoized(stones, num_of_blinks):
    """
    Performs the blinking process for the specified number of blinks, with memoization.
    """
    memo = {}  # Cache for processed stones
    for _ in range(num_of_blinks):
        stones = blink(stones, memo)
    return sum(stones.values())

def main(num_of_blinks):
    """
    Main function to read the input and calculate the number of stones after the given blinks.
    """
    stones = extract_data('input')  
    total_stones = count_stones_memoized(stones, num_of_blinks)
    print(total_stones)

if __name__ == '__main__':
    num_of_blinks = 75
    main(num_of_blinks)
