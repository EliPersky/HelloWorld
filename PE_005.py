from primeFactors import primeFactors
n = 20
inputs = range(2, n)

primefacs = {}

for i in inputs:
    pfs = primeFactors(i)
    for f in pfs:
        if f in primefacs:
            primefacs[f] = max(primefacs[f], pfs[f])
        else:
            primefacs[f] = pfs[f]

primes = list(map(int, list(primefacs)))
powers = [primefacs[i] for i in list(primefacs)]

smallestMult = 1
for i in range(len(primes)):
    smallestMult *= primes[i] ** powers[i]

print(smallestMult)

# 232792560
