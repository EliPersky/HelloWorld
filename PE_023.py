n = 28123

abs = []

for i in range(1, n + 1):
    divsum = 0
    for j in range(1,  int(i/2) + 1):
        if i % j == 0:
            divsum += j

            if divsum > i:
                abs.append(i)
                break

reachable = []

for i in range(len(abs)):
    if abs[i] > n/2:
        break
    for j in range(i, len(abs)):
        if abs[i] + abs[j] > n:
            break
        reachable.append(abs[i] + abs[j])

reachable = set(reachable)


print(int(0.5 * n * (n + 1) - sum(reachable)))

# 4179871

