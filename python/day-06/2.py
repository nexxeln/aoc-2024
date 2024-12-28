DIRECTIONS = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}
TURNS = {"^": ">", ">": "v", "v": "<", "<": "^"}


def simulate(grid, obstacle, bounds, start_pos, start_dir):
    pos = start_pos
    direction = start_dir
    turns = {(pos, direction)}

    while True:
        x, y = pos
        dx, dy = DIRECTIONS[direction]
        next_pos = (x + dx, y + dy)

        if not (0 <= next_pos[0] <= bounds[0] and 0 <= next_pos[1] <= bounds[1]):
            return False

        if next_pos == obstacle or (next_pos in grid and grid[next_pos] == "#"):
            direction = TURNS[direction]
            state = (pos, direction)
            if state in turns:
                return True
            turns.add(state)
        else:
            pos = next_pos


def loop(grid):
    bounds = (max(x for x, _ in grid), max(y for _, y in grid))
    start_pos = next(pos for pos, c in grid.items() if c in "^v<>")
    start_dir = grid[start_pos]
    candidates = set()
    pos, direction = start_pos, start_dir

    valid_positions = {
        (x, y)
        for x in range(bounds[0] + 1)
        for y in range(bounds[1] + 1)
        if (x, y) not in grid and (x, y) != start_pos
    }

    while True:
        x, y = pos
        dx, dy = DIRECTIONS[direction]
        next_pos = (x + dx, y + dy)

        if not (0 <= next_pos[0] <= bounds[0] and 0 <= next_pos[1] <= bounds[1]):
            break

        if next_pos in valid_positions:
            candidates.add(next_pos)

        if next_pos in grid and grid[next_pos] == "#":
            direction = TURNS[direction]
        else:
            pos = next_pos

    return sum(simulate(grid, pos, bounds, start_pos, start_dir) for pos in candidates)


with open(0) as f:
    grid = {
        (x, y): c
        for y, row in enumerate(f.read().splitlines())
        for x, c in enumerate(row)
        if c in "^v<>#"
    }
    print(loop(grid))
