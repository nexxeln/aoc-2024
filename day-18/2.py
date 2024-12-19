from collections import deque

coords = [tuple(map(int, line.strip().split(","))) for line in open(0)]


def bfs(size, blocked, start=(0, 0)):
    queue = deque([(start, 0)])
    seen = {start}
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        (x, y), steps = queue.popleft()
        if (x, y) == (size, size):
            return True

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
    return False


def find_blocking_coord(size):
    blocked = set()
    for coord in coords[:-1]:
        blocked.add(coord)
        if not bfs(size, blocked):
            return coord


print("Test case:", find_blocking_coord(6))
print("Real input:", find_blocking_coord(70))
