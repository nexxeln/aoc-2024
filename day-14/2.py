def standard_deviation(positions):
    xs, ys = zip(*positions)
    x_mean = sum(xs) / len(xs)
    y_mean = sum(ys) / len(ys)

    x_var = sum((x - x_mean) ** 2 for x in xs) / len(xs)
    y_var = sum((y - y_mean) ** 2 for y in ys) / len(ys)

    return (x_var + y_var) ** 0.5


def print_positions(positions, width=101, height=103):
    xs, ys = zip(*positions)
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    grid = [["."] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]

    for x, y in positions:
        grid[y - min_y][x - min_x] = "#"

    return "\n".join("".join(row) for row in grid)


def solve(data, width=101, height=103, max_seconds=20000):
    min_deviation = float("inf")
    best_time = 0
    prev_deviation = float("inf")
    best_positions = None

    for s in range(max_seconds):
        positions = []
        for line in data:
            p, v = line.split()
            px, py = map(int, p[2:].split(","))
            vx, vy = map(int, v[2:].split(","))

            x = (px + vx * s) % width
            y = (py + vy * s) % height
            positions.append((x, y))

        deviation = standard_deviation(positions)

        if deviation < min_deviation:
            min_deviation = deviation
            best_time = s
            best_positions = positions

        if deviation < prev_deviation * 0.7 and deviation < width / 4:
            print(f"Time: {s}, Deviation: {deviation}")
            print(print_positions(positions))
            print()

        prev_deviation = deviation

    print(print_positions(best_positions))
    return best_time


with open(0) as f:
    data = f.read().splitlines()
    print(solve(data))
