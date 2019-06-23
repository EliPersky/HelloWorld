n = 20

prod = 1
for i in range(n):
    prod *= 2 * n - i
for i in range(n):
    prod /= i + 1

print(int(prod))

# 137846528820
