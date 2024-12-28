DIRECTIONS = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}
TURNS = {"^": ">", ">": "v", "v": "<", "<": "^"}


def simulate(grid):
    pos = next(pos for pos, c in grid.items() if c in "^v<>")
    direction = grid[pos]
    visited = {pos}
    bounds = (max(x for x, _ in grid), max(y for _, y in grid))

    while True:
        x, y = pos
        dx, dy = DIRECTIONS[direction]
        next_pos = (x + dx, y + dy)

        if not (0 <= next_pos[0] <= bounds[0] and 0 <= next_pos[1] <= bounds[1]):
            break

        if next_pos in grid and grid[next_pos] == "#":
            direction = TURNS[direction]
        else:
            pos = next_pos
            visited.add(pos)

    return len(visited)


with open(0) as f:
    grid = {
        (x, y): c
        for y, row in enumerate(f.read().splitlines())
        for x, c in enumerate(row)
        if c in "^v<>#"
    }
    print(simulate(grid))
