from primeFactors import primeFactors
from functools import reduce

numdivs = 0
n = 500
i = 2

while numdivs <= n:
    p = primeFactors(i * (i + 1) / 2)
    if len(p) == 1:
        numdivs = list(p.values())[0] + 1
    else:
        numdivs = reduce(lambda x, y: x * y, [j + 1 for j in list(p.values())])
    i += 1

print(i * (i - 1) // 2)

# 76576500
