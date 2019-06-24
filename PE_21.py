n = 10000

ams = []


def divsum(i):
    tot = 0
    for j in range(1, i):
        if i % j == 0:
            tot += j
    return tot


for i in range(1, n):
    if i not in ams:
        ds = divsum(i)
        if divsum(ds) == i and ds != i:
            ams.append(i)
            if ds < n:
                ams.append(ds)


print(sum(ams))

# 31626
