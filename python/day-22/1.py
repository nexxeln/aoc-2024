def next_secret(n):
    n ^= (n * 64) % 16777216
    n ^= (n // 32) % 16777216
    n ^= (n * 2048) % 16777216

    return n


def get_nth_secret(start, n):
    secret = start
    for _ in range(n):
        secret = next_secret(secret)
    return secret


print(sum(get_nth_secret(int(n), 2000) for n in open(0)))
