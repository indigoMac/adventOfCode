def searchWord(grid, word):
    """
    Search for all "X-MAS" patterns in the grid.
    """
    count = 0
    n, m = len(grid), len(grid[0])

    for i in range(1, n - 1):  # Avoid checking edges
        for j in range(1, m - 1):  # Avoid checking edges
            if grid[i][j] == word[1]:  # Check for the center "A"
                if isXMASPattern(grid, i, j, word):
                    count += 1

    return count


def isXMASPattern(grid, x, y, word):
    """
    Check if an "X-MAS" pattern exists with the center at (x, y).
    """
    # Check positions for the "M" and "S" around the center "A"
    try:
        return (
            grid[x - 1][y - 1] == word[0] and  # Top-left "M"
            grid[x + 1][y - 1] == word[0] and  # Bottom-left "M"
            grid[x - 1][y + 1] == word[2] and  # Top-right "S"
            grid[x + 1][y + 1] == word[2]      # Bottom-right "S"
        ) or (
            grid[x - 1][y - 1] == word[2] and  # Top-left "S"
            grid[x + 1][y - 1] == word[2] and  # Bottom-left "S"
            grid[x - 1][y + 1] == word[0] and  # Top-right "M"
            grid[x + 1][y + 1] == word[0]      # Bottom-right "M"
        ) or (
            grid[x - 1][y - 1] == word[2] and  # Top-left "S"
            grid[x + 1][y - 1] == word[0] and  # Bottom-left "M"
            grid[x - 1][y + 1] == word[2] and  # Top-right "S"
            grid[x + 1][y + 1] == word[0]      # Bottom-right "M"
        ) or (
            grid[x - 1][y - 1] == word[0] and  # Top-left "M"
            grid[x + 1][y - 1] == word[2] and  # Bottom-left "S"
            grid[x - 1][y + 1] == word[0] and  # Top-right "M"
            grid[x + 1][y + 1] == word[2]      # Bottom-right "S"
        )
    except IndexError:
        # Handle edge cases where indices are out of bounds
        return False


if __name__ == "__main__":
    word_search = []

    with open('day_4/input.txt', 'r') as file:
        for lines in file:
            word_search.append(list(lines.strip('\n')))

    grid = word_search
    word = "MAS"

    ans = searchWord(grid, word)
    print(ans)
