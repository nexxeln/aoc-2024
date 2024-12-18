def find_robot(grid):
    return next(
        (r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "@"
    )


def get_next_pos(pos, d):
    r, c = pos
    return {">": (r, c + 1), "<": (r, c - 1), "^": (r - 1, c), "v": (r + 1, c)}[d]


def get_cell(grid, pos):
    r, c = pos
    if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
        return "#"
    return grid[r][c]


def check_move(grid, pos, d):
    moves = []
    while True:
        next_pos = get_next_pos(pos, d)
        cell = get_cell(grid, next_pos)
        if cell == ".":
            moves.append((pos, next_pos))
            return moves
        if cell != "O":
            return None
        moves.append((pos, next_pos))
        pos = next_pos


def make_move(grid, robot_pos, d):
    moves = check_move(grid, robot_pos, d)
    if not moves:
        return grid, robot_pos

    new_grid = [row.copy() for row in grid]
    for f, t in moves[::-1]:
        new_grid[t[0]][t[1]] = grid[f[0]][f[1]]
        new_grid[f[0]][f[1]] = "."
    return new_grid, moves[0][1]


def calculate_gps(grid):
    return sum(
        100 * r + c
        for r, row in enumerate(grid)
        for c, ch in enumerate(row)
        if ch == "O"
    )


grid = []
moves = ""
for line in open(0):
    if line[0] in ".#@O":
        grid.append(list(line.strip()))
    elif line[0] in "<>^v":
        moves += line.strip()

pos = find_robot(grid)
for m in moves:
    grid, pos = make_move(grid, pos, m)

print(calculate_gps(grid))
