
longchain = 0
val = 0
n = 1000000

chains = {}

for i in range(1, n):
    chain = 0
    c = i
    while c > 1:
        if str(c) in chains:
            chains[str(i)] = chain + chains[str(c)]
            break
        elif c % 2 == 0:
            c //= 2
        else:
            c = 3 * c + 1
        chain += 1
    else:
        chains[str(i)] = chain

print(list(chains)[list(chains.values()).index(max(list(chains.values())))])

# 837799
