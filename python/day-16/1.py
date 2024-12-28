from heapq import heappush, heappop

grid = [list(line.strip()) for line in open(0)]
H, W = len(grid), len(grid[0])

start = next((i, j) for i in range(H) for j in range(W) if grid[i][j] == "S")
end = next((i, j) for i in range(H) for j in range(W) if grid[i][j] == "E")

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solve():
    queue = [(0, start[0], start[1], 0)]
    seen = set()

    while queue:
        cost, x, y, d = heappop(queue)

        if (x, y) == end:
            return cost

        if (x, y, d) in seen:
            continue
        seen.add((x, y, d))

        nx, ny = x + DIRS[d][0], y + DIRS[d][1]
        if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != "#":
            heappush(queue, (cost + 1, nx, ny, d))

        for nd in [(d - 1) % 4, (d + 1) % 4]:
            heappush(queue, (cost + 1000, x, y, nd))


print(solve())
