def get_heights(lines, top):
    width = len(lines[0])
    heights = []

    for col in range(width):
        height = 0
        if top:
            for row in range(len(lines)):
                if lines[row][col] == "#":
                    height = row + 1
        else:
            for row in range(len(lines) - 1, -1, -1):
                if lines[row][col] == "#":
                    height = len(lines) - row
        heights.append(height)

    return heights


locks = []
keys = []
current = []

for group in open(0).read().strip().split("\n\n"):
    lines = group.splitlines()
    if lines:
        is_lock = lines[0].startswith("#")
        heights = get_heights(lines, is_lock)
        (locks if is_lock else keys).append(heights)

print(
    sum(
        1
        for lock in locks
        for key in keys
        if all(lh + kh <= 7 for lh, kh in zip(lock, key))
    )
)
