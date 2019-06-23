f = open('PE_013_data.txt', 'r')
nums = []
n = 100
d = 10
for line in f:
    nums.append(int(line))
f.close()

total = sum(nums)

print(int(str(total)[0:d]))

# 5537376230
