def get_neighbors(x, y, grid):
    return [
        (x + dx, y + dy)
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]
        if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0])
    ]


def find_region(start_x, start_y, grid, visited):
    char, region = grid[start_x][start_y], {(start_x, start_y)}
    to_visit = [(start_x, start_y)]
    while to_visit:
        x, y = to_visit.pop()
        if (x, y) not in visited and grid[x][y] == char:
            region.add((x, y))
            visited.add((x, y))
            to_visit.extend(get_neighbors(x, y, grid))
    return region


def pad_grid(grid):
    w, h = len(grid[0]) + 2, len(grid) + 2
    new_grid = [["."] * w for _ in range(h)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            new_grid[i + 1][j + 1] = grid[i][j]
    return new_grid


def count_sides(region, grid):
    sides = 0
    for x, y in region:
        for dx, dy, cond in [
            (
                -1,
                0,
                lambda: grid[x - 1][y - 1] == grid[x][y]
                or grid[x][y - 1] != grid[x][y],
            ),
            (
                0,
                -1,
                lambda: grid[x - 1][y - 1] == grid[x][y]
                or grid[x - 1][y] != grid[x][y],
            ),
            (
                1,
                0,
                lambda: grid[x + 1][y - 1] == grid[x][y]
                or grid[x][y - 1] != grid[x][y],
            ),
            (
                0,
                1,
                lambda: grid[x - 1][y + 1] == grid[x][y]
                or grid[x - 1][y] != grid[x][y],
            ),
        ]:
            if grid[x + dx][y + dy] != grid[x][y] and cond():
                sides += 1
    return sides


def solve(grid):
    padded = pad_grid(grid)
    visited, total = set(), 0
    for i in range(1, len(padded) - 1):
        for j in range(1, len(padded[0]) - 1):
            if (i, j) not in visited and padded[i][j] != ".":
                region = find_region(i, j, padded, visited)
                area = len(region)
                sides = count_sides(region, padded)
                total += area * sides
    return total


grid = [list(line.strip()) for line in open(0)]
print(solve(grid))
