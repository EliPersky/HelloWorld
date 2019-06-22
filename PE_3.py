
n = 600851475143

while True:
    for i in range(2, n//2):
        if n % i == 0:
            n //= i
            break
    else:
        break

print(n)

# 6857
