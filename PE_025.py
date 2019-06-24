n = 1000

fib = [1, 1]
i = 2

while len(str(fib[1])) < n:
    fib = [fib[1], fib[0] + fib[1]]
    i += 1

print(i)

# 4782
