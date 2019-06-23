
n = 1000

factors = [3, 5]

total = 0

for i in range(1000):
    if len(list(filter(lambda fac: i % fac == 0, factors))) > 0:
        total += i

print(total)

# 233168
