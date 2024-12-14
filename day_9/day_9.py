def extract_data(filename):
    """
    Reads the disk map data from a file and returns it as a string.
    """
    with open(f"day_9/{filename}.txt", "r") as file:
        return file.read().strip('\n')


def get_disk_blocks(disk_map):
    """
    Converts the dense disk map into a string representation of disk blocks.

    Each file is represented by its ID (0, 1, 2, ...) and free space is represented by '.'
    """
    file_id = 0
    disk_blocks = []
    for i in range(0, len(disk_map), 2):
        file_length = int(disk_map[i])
        free_length = int(disk_map[i + 1]) if i + 1 < len(disk_map) else 0
        disk_blocks.extend([str(file_id)] * file_length)  # Add file blocks
        disk_blocks.extend(['.'] * free_length)  # Add free space
        file_id += 1
    return disk_blocks


def compact_disk(disk_blocks):
    """
    Compacts the disk blocks by moving each file block from the end to the leftmost free space.

    Returns the final state of the disk after compaction.
    """
    for i in range(len(disk_blocks) - 1, -1, -1):
        if disk_blocks[i] != '.':
            for j in range(len(disk_blocks)):
                if disk_blocks[j] == '.':
                    disk_blocks[j] = disk_blocks[i]
                    disk_blocks[i] = '.'
                    continue
                if j >= i:
                    return disk_blocks


def calculate_checksum(disk_blocks):
    """
    Calculates the filesystem checksum by summing up (position * file ID) for all file blocks.
    """
    checksum = 0
    for position, block in enumerate(disk_blocks):
        if block != '.':  # Only include file blocks
            checksum += position * int(block)
    return checksum


if __name__ == "__main__":
    # Step 1: Load the disk map data
    disk_map = extract_data("input copy")

    # Step 2: Convert the dense disk map into disk blocks
    disk_blocks = get_disk_blocks(disk_map)
    print(f"Initial Disk Blocks: {''.join(disk_blocks)}")

    # Step 3: Compact the disk by moving blocks to the leftmost free space
    compacted_disk = compact_disk(disk_blocks)
    print(f"\nCompacted Disk Blocks: {''.join(compacted_disk)}")

    # Step 4: Calculate the checksum
    checksum = calculate_checksum(compacted_disk)
    print(f"\nFilesystem Checksum: {checksum}")
