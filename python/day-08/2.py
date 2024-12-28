def is_collinear(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)


grid = [list(line.strip()) for line in open(0)]
height, width = len(grid), len(grid[0])

antennas = {}
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c != ".":
            if c not in antennas:
                antennas[c] = []
            antennas[c].append((x, y))

antinodes = set()
for positions in antennas.values():
    for y in range(height):
        for x in range(width):
            if any(
                is_collinear((x, y), *pair)
                for pair in (
                    (positions[i], positions[j])
                    for i in range(len(positions))
                    for j in range(i + 1, len(positions))
                )
            ):
                antinodes.add((x, y))

print(len(antinodes))
