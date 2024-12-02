def is_safe(nums):
    if len(set(nums)) != len(nums):
        return False
    diffs = [b - a for a, b in zip(nums[:-1], nums[1:])]

    incdec = all(d > 0 for d in diffs) or all(d < 0 for d in diffs)
    limits = all(1 <= abs(d) <= 3 for d in diffs)

    return incdec and limits


with open(0) as f:
    print(sum(1 for line in f if is_safe([int(x) for x in line.split()])))
