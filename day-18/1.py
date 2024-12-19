from collections import deque

coords = [tuple(map(int, line.strip().split(","))) for line in open(0)]


def bfs(size, num_blocks, start=(0, 0)):
    blocked = set(coords[:num_blocks])
    queue = deque([(start, 0)])
    seen = {start}
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        (x, y), steps = queue.popleft()
        if (x, y) == (size, size):
            return steps

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            pos = (nx, ny)
            if (
                0 <= nx <= size
                and 0 <= ny <= size
                and pos not in blocked
                and pos not in seen
            ):
                seen.add(pos)
                queue.append((pos, steps + 1))


print("Test case:", bfs(6, 12))
print("Real input:", bfs(70, 1024))
