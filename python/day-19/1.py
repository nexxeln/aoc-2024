def solve(pattern, towels, cache=None):
    if cache is None:
        cache = {}
    if not pattern:
        return True
    if pattern in cache:
        return cache[pattern]

    cache[pattern] = any(
        pattern.startswith(towel) and solve(pattern[len(towel) :], towels, cache)
        for towel in towels
    )
    return cache[pattern]


lines = [line.strip() for line in open(0)]
towels = {t.strip() for t in lines[0].split(",")}
patterns = [line.strip() for line in lines[2:]]

print(sum(1 for pattern in patterns if solve(pattern, towels)))
