total = 0

fib = [1, 2]

n = 4e6

while fib[1] <= n:
    if fib[1] % 2 == 0:
        total += fib[1]
    fib = [fib[1], sum(fib)]

print(total)

# 4613732
