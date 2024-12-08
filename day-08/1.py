def get_antinodes(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return [(2 * x2 - x1, 2 * y2 - y1), (2 * x1 - x2, 2 * y1 - y2)]


grid = [list(line) for line in open(0)]
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
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            for x, y in get_antinodes(positions[i], positions[j]):
                if 0 <= x < width and 0 <= y < height:
                    antinodes.add((x, y))

print(len(antinodes))
