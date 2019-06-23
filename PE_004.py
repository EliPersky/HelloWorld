largest = 0
digits = 3
rmin = 10 ** (digits-1)
rmax = 10 ** digits - 1

for i in range(rmax, rmin - 1, -1):
    for j in range(i, rmin - 1, -1):
        if i * j > largest:
            if list(str(i * j)) == list(reversed(str(i * j))):
                largest = i * j
        else:
            break

print(largest)

# 906609
