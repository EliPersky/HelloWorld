
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = 1
date = 1
month = 1
year = 1900

total = 0

while year < 2001:

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        mls = days2
    else:
        mls = days

    if day == 7 and date == 1 and year >= 1901:
        total += 1

    if date == mls[month - 1]:
        date = 0
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    else:
        date += 1

    if day == 7:
        day = 1
    else:
        day += 1

print(total)

# 171
