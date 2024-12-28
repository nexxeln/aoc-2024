def transform_map(grid):
    expansion = {"#": "##", "O": "[]", ".": "..", "@": "@."}
    return [list("".join(expansion[ch] for ch in row)) for row in grid]


def find_robot(grid):
    return next(
        (r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "@"
    )


def make_move(grid, pos, d):
    r, c = pos
    dr = {"^": -1, "v": 1}.get(d, 0)
    dc = {"<": -1, ">": 1}.get(d, 0)
    targets = [(r, c)]

    for cr, cc in targets:
        nr, nc = cr + dr, cc + dc
        if (nr, nc) in targets:
            continue
        char = grid[nr][nc]
        if char == "#":
            return grid, pos
        if char == "[":
            targets.extend([(nr, nc), (nr, nc + 1)])
        if char == "]":
            targets.extend([(nr, nc), (nr, nc - 1)])

    new_grid = [row.copy() for row in grid]
    new_grid[r][c] = "."
    new_grid[r + dr][c + dc] = "@"
    for br, bc in targets[1:]:
        new_grid[br][bc] = "."
    for br, bc in targets[1:]:
        new_grid[br + dr][bc + dc] = grid[br][bc]

    return new_grid, (r + dr, c + dc)


def calculate_gps(grid):
    return sum(
        100 * r + c
        for r, row in enumerate(grid)
        for c, ch in enumerate(row)
        if ch == "["
    )


grid = []
moves = ""
for line in open(0):
    if line[0] in ".#@O":
        grid.append(list(line.strip()))
    elif line[0] in "<>^v":
        moves += line.strip()

grid = transform_map(grid)
pos = find_robot(grid)
for m in moves:
    grid, pos = make_move(grid, pos, m)

print(calculate_gps(grid))
