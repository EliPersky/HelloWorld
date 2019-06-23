
words1 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
words2 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
words3 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
words4 = ["hundred", "thousand"]

total = 0

for i in range(1, 1001):
    i = str(i)
    if len(i) == 1:
        total += len(words1[int(i)])
    if len(i) == 2:
        a = int(list(i)[0])
        b = int(list(i)[1])
        if a == 1:
            total += len(words2[b])
        else:
            total += len(words3[a - 2]) + len(words1[b])
    if len(i) == 3:
        a = int(list(i)[0])
        b = int(list(i)[1])
        c = int(list(i)[2])
        total += len(words1[a]) + len(words4[0])
        if b == 0:
            if c != 0:
                total += 3 + len(words1[c])
        elif b == 1:
            total += 3 + len(words2[c])
        else:
            total += 3 + len(words3[b - 2]) + len(words1[c])
    if len(i) == 4:
        total += len(words1[1]) + len(words4[1])

print(total)

# 21124
