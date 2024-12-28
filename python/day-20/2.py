from collections import deque


def bfs(start, grid, through_walls=False, max_steps=float("inf")):
    h, w, dist = len(grid), len(grid[0]), {start: 0}
    q = deque([(start, 0)])

    while q:
        pos, d = q.popleft()
        if d == max_steps:
            continue

        for ny, nx in [
            (pos[0] + dy, pos[1] + dx) for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ]:
            if (
                0 <= ny < h
                and 0 <= nx < w
                and (ny, nx) not in dist
                and (through_walls or grid[ny][nx] == ".")
            ):
                dist[(ny, nx)] = d + 1
                q.append(((ny, nx), d + 1))

    return {k: v for k, v in dist.items() if grid[k[0]][k[1]] == "."}


def solve(lines):
    grid = [list(line) for line in lines]
    start = next(
        (i, j) for i, row in enumerate(grid) for j, c in enumerate(row) if c == "S"
    )
    end = next(
        (i, j) for i, row in enumerate(grid) for j, c in enumerate(row) if c == "E"
    )
    grid[start[0]][start[1]] = grid[end[0]][end[1]] = "."

    start_dists = bfs(start, grid)
    end_dists = bfs(end, grid)
    normal_time = start_dists.get(end, float("inf"))

    savings = []
    for pos in set(start_dists) & set(end_dists):
        for end_pos, cheat_steps in bfs(pos, grid, True, 20).items():
            if end_pos in end_dists and end_pos != pos:
                savings.append(
                    normal_time - (start_dists[pos] + cheat_steps + end_dists[end_pos])
                )

    return sum(1 for x in savings if x >= 100)


print(solve([line.strip() for line in open(0)]))
