with open(0) as f:
    grid = f.read().splitlines()
    rows, cols = len(grid), len(grid[0])
    count = 0

    for i in range(rows - 2):
        for j in range(1, cols - 1):
            d1 = "".join(grid[i + k][j - 1 + k] for k in range(3))
            d2 = "".join(grid[i + k][j + 1 - k] for k in range(3))

            valid = {"MAS", "SAM"}
            if (d1 in valid or d1[::-1] in valid) and (
                d2 in valid or d2[::-1] in valid
            ):
                count += 1

print(count)
