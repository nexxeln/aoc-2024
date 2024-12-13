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


def get_perimeter(region, grid):
    perimeter = 0
    for x, y in region:
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if (
                nx < 0
                or nx >= len(grid)
                or ny < 0
                or ny >= len(grid[0])
                or (nx, ny) not in region
            ):
                perimeter += 1
    return perimeter


def solve(grid):
    visited, regions = set(), []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited:
                regions.append(find_region(i, j, grid, visited))
    return sum(len(r) * get_perimeter(r, grid) for r in regions)


grid = [list(line.strip()) for line in open(0)]
print(solve(grid))
