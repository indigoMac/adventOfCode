from collections import Counter
from multiprocessing import Pool, cpu_count

def extract_data(file):
    """
    Reads the stone data from the input file and returns it as a Counter.
    """
    with open(f"day_11/{file}.txt", 'r') as file:
        stones = file.read().strip('\n').split(' ')
        return Counter(stones)

def process_chunk(chunk):
    """
    Processes a chunk of stones and returns the updated stone counts.
    Each chunk is a dictionary of {stone_value: count}.
    """
    updated_stones = Counter()
    for stone, count in chunk.items():
        stone = str(stone)
        if stone == '0':
            updated_stones['1'] += count
        elif len(stone) % 2 == 0:
            mid = len(stone) // 2
            left, right = stone[:mid], str(int(stone[mid:]))
            updated_stones[left] += count
            updated_stones[right] += count
        else:
            new_stone = str(int(stone) * 2024)
            updated_stones[new_stone] += count
    return updated_stones

def split_into_chunks(stones, num_chunks):
    """
    Splits the stone dictionary into smaller chunks for parallel processing.
    """
    chunk_size = len(stones) // num_chunks
    items = list(stones.items())
    return [dict(items[i:i + chunk_size]) for i in range(0, len(items), chunk_size)]

def blink_parallel(stones, num_processes):
    """
    Processes stones using parallel processing with the specified number of processes.
    """
    # Split stones into chunks
    chunks = split_into_chunks(stones, num_processes)
    
    # Use multiprocessing Pool to process chunks in parallel
    with Pool(num_processes) as pool:
        results = pool.map(process_chunk, chunks)
    
    # Combine results from all processes
    updated_stones = Counter()
    for result in results:
        updated_stones.update(result)
    return updated_stones

def count_stones_parallel(stones, num_of_blinks):
    """
    Blinks the stones multiple times using parallel processing.
    """
    num_processes = min(cpu_count(), len(stones))  # Use available CPU cores
    for _ in range(num_of_blinks):
        stones = blink_parallel(stones, num_processes)
    return sum(stones.values())

def main(num_of_blinks):
    """
    Main function to read the input and calculate the number of stones after the given blinks.
    """
    stones = extract_data('input copy')  # Replace 'input' with your file name
    total_stones = count_stones_parallel(stones, num_of_blinks)
    print(total_stones)

if __name__ == '__main__':
    num_of_blinks = 25
    main(num_of_blinks)
