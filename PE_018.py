n = 15

tri = []

tri.append([75])
tri.append([int(x) for x in '95 64'.split(' ')])
tri.append([int(x) for x in '17 47 82'.split(' ')])
tri.append([int(x) for x in '18 35 87 10'.split(' ')])
tri.append([int(x) for x in '20 04 82 47 65'.split(' ')])
tri.append([int(x) for x in '19 01 23 75 03 34'.split(' ')])
tri.append([int(x) for x in '88 02 77 73 07 63 67'.split(' ')])
tri.append([int(x) for x in '99 65 04 28 06 16 70 92'.split(' ')])
tri.append([int(x) for x in '41 41 26 56 83 40 80 70 33'.split(' ')])
tri.append([int(x) for x in '41 48 72 33 47 32 37 16 94 29'.split(' ')])
tri.append([int(x) for x in '53 71 44 65 25 43 91 52 97 51 14'.split(' ')])
tri.append([int(x) for x in '70 11 33 28 77 73 17 78 39 68 17 57'.split(' ')])
tri.append([int(x) for x in '91 71 52 38 17 14 91 43 58 50 27 29 48'.split(' ')])
tri.append([int(x) for x in '63 66 04 68 89 53 67 30 73 16 69 87 40 31'.split(' ')])
tri.append([int(x) for x in '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'.split(' ')])

for i in range(1, n):
    for j in range(n - i):
        tri[n - i - 1][j] = tri[n - i - 1][j] + max(tri[n - i][j], tri[n - i][j + 1])

print(tri[0][0])

# 1074
