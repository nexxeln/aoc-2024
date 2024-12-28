def solve(pattern, towels, cache=None):
    if cache is None:
        cache = {}
    if not pattern:
        return 1
    if pattern in cache:
        return cache[pattern]

    cache[pattern] = sum(
        solve(pattern[len(towel) :], towels, cache)
        for towel in towels
        if pattern.startswith(towel)
    )
    return cache[pattern]


lines = [line.strip() for line in open(0)]
towels = {t.strip() for t in lines[0].split(",")}
patterns = [line.strip() for line in lines[2:]]

print(sum(solve(pattern, towels) for pattern in patterns))
