from itertools import groupby


def parse_line(line):
    x, y = [
        int("".join(c for c in part if c.isdigit() or c == "-"))
        for part in line.split(",")
    ]

    if line.startswith("Prize"):
        x += 10_000_000_000_000
        y += 10_000_000_000_000
    return x, y


def solve_machine(lines):
    ax, ay = parse_line(lines[0])
    bx, by = parse_line(lines[1])
    px, py = parse_line(lines[2])

    det = ax * by - bx * ay
    if det == 0:
        return 0

    n = (px * by - bx * py) / det
    m = (ax * py - px * ay) / det

    if n.is_integer() and m.is_integer() and n >= 0 and m >= 0:
        return int(3 * n + m)
    return 0


data = [line.strip() for line in open(0)]
machines = [list(g) for k, g in groupby(data, bool) if k]

print(sum(solve_machine(machine) for machine in machines))