from math import sqrt


def primeSieve(n):
    n = int(n)
    if n % 2:
        n += 1
    sieve = [True, False] * (n // 2 - 1)

    for p in range(0, int(sqrt(n)) - 2, 2):
        if sieve[p]:
            for i in range((p + 3) * (p + 3), n, 2 * (p + 3)):
                sieve[i - 3] = False

    return [2] + list(filter(lambda x: sieve[x - 3], list(range(3, n+1))))
