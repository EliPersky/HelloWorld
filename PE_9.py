n = 1000

for i in range(n):
    for j in range(i + 1, (n - i) // 2 + 1):
        if i ** 2 + j ** 2 == (n - i - j) ** 2:
            a = i
            b = j
            break
            break

print(a * b * (n - a - b))

# 31875000
