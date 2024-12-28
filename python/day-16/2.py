from heapq import heappush, heappop

grid = [list(line.strip()) for line in open(0)]
H, W = len(grid), len(grid[0])

start = next((i, j) for i in range(H) for j in range(W) if grid[i][j] == "S")
end = next((i, j) for i in range(H) for j in range(W) if grid[i][j] == "E")

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solve():
    queue = [(0, start[0], start[1], 0, 1)]
    lowest_cost = {(start[0], start[1], 0, 1): 0}
    backtrack = {}
    best_cost = float("inf")
    end_states = set()

    while queue:
        cost, r, c, dr, dc = heappop(queue)

        if cost > lowest_cost.get((r, c, dr, dc), float("inf")):
            continue

        if grid[r][c] == "E":
            if cost > best_cost:
                break
            best_cost = cost
            end_states.add((r, c, dr, dc))
            continue

        moves = [
            (cost + 1, r + dr, c + dc, dr, dc),
            (cost + 1000, r, c, dc, -dr),
            (cost + 1000, r, c, -dc, dr),
        ]

        for new_cost, nr, nc, ndr, ndc in moves:
            if not (0 <= nr < H and 0 <= nc < W) or grid[nr][nc] == "#":
                continue

            lowest = lowest_cost.get((nr, nc, ndr, ndc), float("inf"))
            if new_cost > lowest:
                continue

            if new_cost < lowest:
                backtrack[(nr, nc, ndr, ndc)] = set()
                lowest_cost[(nr, nc, ndr, ndc)] = new_cost

            if (nr, nc, ndr, ndc) not in backtrack:
                backtrack[(nr, nc, ndr, ndc)] = set()
            backtrack[(nr, nc, ndr, ndc)].add((r, c, dr, dc))
            heappush(queue, (new_cost, nr, nc, ndr, ndc))

    states = list(end_states)
    seen = set(end_states)
    i = 0

    while i < len(states):
        state = states[i]
        i += 1
        for prev_state in backtrack.get(state, []):
            if prev_state in seen:
                continue
            seen.add(prev_state)
            states.append(prev_state)

    return len({(r, c) for r, c, _, _ in seen})


print(solve())
