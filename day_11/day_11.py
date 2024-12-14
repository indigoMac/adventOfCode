def extract_data(file):
    with open(f"day_11/{file}.txt", 'r') as file:
        return file.read().strip('\n').split(' ')

def blink(stones):
    updated_stones = []
    for stone in stones:
        stone = str(stone)
        if stone == '0':
            updated_stones.append('1')
        elif len(stone) % 2 == 0:
            mid = len(stone) // 2
            stone1, stone2 = stone[:mid], stone[mid:]
            updated_stones.append(stone1)
            updated_stones.append(int(stone2))
        else:
            updated_stones.append(int(stone) * 2024)
    return updated_stones

def count_stones(stones, num_of_blinks):
    for i in range(num_of_blinks):
        stones = blink(stones)
        # print(stones)
    return len(stones)

def main(num_of_blinks):
    stones = extract_data('input')

    num_of_stones = count_stones(stones, num_of_blinks)
    print(num_of_stones)

if __name__ == '__main__':
    num_of_blinks = 75
    main(num_of_blinks)