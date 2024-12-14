def solve(data, width=101, height=103, seconds=100):
    mid_x, mid_y = width // 2, height // 2
    quads = [0] * 4

    for line in data:
        p, v = line.split()
        px, py = map(int, p[2:].split(","))
        vx, vy = map(int, v[2:].split(","))

        x = (px + vx * seconds) % width
        y = (py + vy * seconds) % height

        if x != mid_x and y != mid_y:
            quad_idx = int(x > mid_x) + 2 * int(y > mid_y)
            quads[quad_idx] += 1

    return quads[0] * quads[1] * quads[2] * quads[3]


with open(0) as f:
    print(solve(f.read().splitlines()))
