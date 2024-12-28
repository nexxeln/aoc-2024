from collections import deque

grid = [[int(c) for c in line.strip()] for line in open(0)]
R, C = len(grid), len(grid[0])


def neighbors(r, c):
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            yield nr, nc


def count_paths(r, c):
    if grid[r][c] != 0:
        return 0

    q = deque([(r, c, tuple([(r, c)]))])
    paths = set()

    while q:
        r, c, path = q.popleft()
        if grid[r][c] == 9:
            paths.add(path)
            continue

        for nr, nc in neighbors(r, c):
            if (nr, nc) not in path and grid[nr][nc] == grid[r][c] + 1:
                q.append((nr, nc, path + ((nr, nc),)))

    return len(paths)


total = sum(count_paths(r, c) for r in range(R) for c in range(C) if grid[r][c] == 0)
print(total)
