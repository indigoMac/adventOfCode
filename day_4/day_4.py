def isValid(x, y, sizeX, sizeY):
    """
    Check if the given coordinate is within the grid bounds.
    """
    return 0 <= x < sizeX and 0 <= y < sizeY


def findWordInDirection(grid, n, m, word, x, y, dirX, dirY):
    """
    Check if the word can be found starting from (x, y) in the given direction (dirX, dirY).
    """
    for index in range(len(word)):
        newX, newY = x + dirX * index, y + dirY * index
        if not isValid(newX, newY, n, m) or grid[newX][newY] != word[index]:
            return False
    return True


def searchWord(grid, word):
    """
    Search for all occurrences of the word in the grid in any direction.
    """
    ans = 0
    n, m = len(grid), len(grid[0])

    # Directions for 8 possible movements
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for i in range(n):
        for j in range(m):
            # Check if the first character matches
            if grid[i][j] == word[0]:  
                for dirX, dirY in directions:
                    if findWordInDirection(grid, n, m, word, i, j, dirX, dirY):
                        ans += 1
    return ans


if __name__ == "__main__":
    word_search = [] 

    with open('day_4/input.txt', 'r') as file:
        for lines in file:
            word_search.append(list(lines.strip('\n')))  

    grid = word_search  # 2D grid of characters
    word = "XMAS"

    ans = searchWord(grid, word)
    print(ans)
