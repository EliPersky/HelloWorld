from math import factorial

n = int(1e6)
d = 10

remaining = list(range(d))

ans = ''

for i in range(d):
    c = (n - 1) // factorial(d - 1 - i)
    n -= c * factorial(d - 1 - i)
    ans += str(remaining[c])
    remaining.remove(remaining[c])


print(ans)

# 2783915460



