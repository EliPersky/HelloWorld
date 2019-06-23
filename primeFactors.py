from math import sqrt
# Returns dictionary of prime factors and powers

def primeFactors(n):
    primefacs = {}
    while n % 2 == 0:
        if '2' in primefacs:
            primefacs['2'] += 1
        else:
            primefacs['2'] = 1
        n //= 2

    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            if str(i) in primefacs:
                primefacs[str(i)] += 1
            else:
                primefacs[str(int(i))] = 1
            n //= i
    if n > 1:
        if str(n) in primefacs:
            primefacs[str(n)] += 1
        else:
            primefacs[str(int(n))] = 1

    return primefacs