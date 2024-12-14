def calculate_sum(length, start_block):
    """
    Calculates the sum of positions occupied by a file's blocks in the disk.

    Args:
        length (int): Number of blocks occupied by the file.
        start_block (int): Starting position of the file's blocks.

    Returns:
        int: Sum of positions occupied by the file's blocks.
    """
    return length * (2 * start_block + length - 1) // 2

def parse_input(file_path):
    """
    Parses the input file and converts it into structured data.

    Args:
        file_path (str): Path to the input file.

    Returns:
        dict: A dictionary representing files and their metadata.
    """
    with open(file_path, "r") as input_file:
        input_data = input_file.read().strip()

    data = list(map(int, input_data))
    data.append(0)  # Append trailing 0 to simplify parsing

    blocks = {}
    for i in range(0, len(data), 2):
        blocks[i // 2] = {
            "l": data[i],        # File length
            "f": data[i + 1],    # Free space length
            "s": [],             # Subfiles moved into this file
        }
    return blocks

def move_files(blocks):
    """
    Moves files into available free space in descending order of file IDs.

    Args:
        yikes (dict): The file metadata dictionary.
    """
    for candidate_id in reversed(blocks):
        candidate = blocks[candidate_id]

        for target_id in blocks:
            # Stop if we've reached a higher ID
            if candidate_id <= target_id:
                break

            target = blocks[target_id]

            # Check if the target has enough free space for the candidate
            if target["f"] >= candidate["l"] > 0:
                # Move the file into the target
                target["s"].append({"l": candidate["l"], "id": candidate_id})
                target["f"] -= candidate["l"]
                candidate["ff"] = candidate["l"]  # Record the moved length
                candidate["l"] = 0  # Mark the candidate as moved
                break

def calculate_checksum(yikes):
    """
    Calculates the checksum of the filesystem.

    Args:
        yikes (dict): The file metadata dictionary.

    Returns:
        int: The checksum of the filesystem.
    """
    checksum = 0
    block = 0

    for file_id, file in yikes.items():
        # Add checksum for unmoved files
        if "ff" in file:
            block += file["ff"]
        else:
            checksum += file_id * calculate_sum(file["l"], block)
            block += file["l"]

        # Add checksum for subfiles moved into this file
        for subfile in file["s"]:
            checksum += subfile["id"] * calculate_sum(subfile["l"], block)
            block += subfile["l"]

        # Add free space to the block counter
        block += file["f"]

    return checksum

def main():
    """
    Main function to execute the disk compaction and checksum calculation.
    """
    input_file_path = "day_9/input copy.txt"

    # Step 1: Parse the input file
    disk_blocks = parse_input(input_file_path)

    # Step 2: Move files to free space
    move_files(disk_blocks)

    # Step 3: Calculate and print the checksum
    checksum = calculate_checksum(disk_blocks)
    print(f"Checksum: {checksum}")

if __name__ == "__main__":
    main()