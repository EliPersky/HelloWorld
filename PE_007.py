n = 10001

primes = [2]

i = 2

while len(primes) < n:
    for p in primes:
        if i % p == 0:
            break
    else:
        primes.append(i)
    i += 1

print(primes[-1])

# 104743
