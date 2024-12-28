def is_safe(nums):
    if len(set(nums)) != len(nums):
        return False
    diffs = [b - a for a, b in zip(nums[:-1], nums[1:])]

    incdec = all(d > 0 for d in diffs) or all(d < 0 for d in diffs)
    limits = all(1 <= abs(d) <= 3 for d in diffs)

    return incdec and limits


def fn(numbers):
    if is_safe(numbers):
        return True
    return any(is_safe(numbers[:i] + numbers[i + 1 :]) for i in range(len(numbers)))


with open(0) as f:
    print(sum(1 for line in f if fn([int(x) for x in line.split()])))
