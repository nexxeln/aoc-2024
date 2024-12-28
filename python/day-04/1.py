with open(0) as f:
    grid = f.read().splitlines()
    rows, cols = len(grid), len(grid[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            for dx, dy in [(0, 1), (1, 1), (1, 0), (1, -1)]:
                if 0 <= i + dx * 3 < rows and 0 <= j + dy * 3 < cols:
                    word = "".join(grid[i + dx * k][j + dy * k] for k in range(4))
                    if word == "XMAS" or word[::-1] == "XMAS":
                        count += 1

print(count)
