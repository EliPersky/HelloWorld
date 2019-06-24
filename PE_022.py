f = open('PE_022_data.txt', 'r')
names = f.read().replace('"', '').split(',')
f.close()

names = sorted(names)

score = 0

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y', 'Z']

for i in range(len(names)):
    for j in range(len(names[i])):
        score += (i + 1) * (letters.index(names[i][j]) + 1)

print(score)

# 871198282
