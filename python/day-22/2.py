def next_secret(n):
    n ^= (n * 64) % 16777216
    n ^= (n // 32) % 16777216
    n ^= (n * 2048) % 16777216

    return n


def get_secrets(start):
    secret = start
    secrets = [secret]
    for _ in range(2000):
        secret = next_secret(secret)
        secrets.append(secret)
    return secrets


def solve(numbers):
    totals = {}
    for num in map(int, numbers):
        prices = [x % 10 for x in get_secrets(num)]

        seen = set()
        for i in range(len(prices) - 4):
            p = prices[i : i + 5]
            seq = tuple(p[j + 1] - p[j] for j in range(4))
            if seq not in seen:
                seen.add(seq)
                totals[seq] = totals.get(seq, 0) + p[-1]

    return max(totals.values())


print(solve(open(0)))
