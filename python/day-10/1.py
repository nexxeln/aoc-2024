from collections import deque

grid = [[int(c) for c in line.strip()] for line in open(0)]
R, C = len(grid), len(grid[0])


def neighbors(r, c):
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            yield nr, nc


def count_nines(r, c):
    if grid[r][c] != 0:
        return 0

    seen = {(r, c)}
    q = deque([(r, c)])
    nines = 0

    while q:
        r, c = q.popleft()
        if grid[r][c] == 9:
            nines += 1
            continue

        for nr, nc in neighbors(r, c):
            if (nr, nc) not in seen and grid[nr][nc] == grid[r][c] + 1:
                seen.add((nr, nc))
                q.append((nr, nc))

    return nines


total = sum(count_nines(r, c) for r in range(R) for c in range(C) if grid[r][c] == 0)
print(total)
