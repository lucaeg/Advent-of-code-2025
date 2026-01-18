file1 = open("day5.txt", "r")
lines = file1.readlines()

intervals = []
numbers = []

for line in lines:
    try:
        number = int(line.strip())
        numbers.append(number)
    except ValueError:
        if line.strip():
            interval = list(map(int, line.strip().split("-")))
            intervals.append(interval)


intervals.sort()

# Initial case
lower = intervals[0][0]
upper = intervals[0][1]
fresh = intervals[0][1] - intervals[0][0] + 1

# Looping
for interval in intervals[1:]:
    if interval[0] <= upper:
        if interval[1] <= upper:
            continue
        else:
            fresh += interval[1] - upper
            upper = interval[1]
    else:
        fresh += interval[1] - interval[0] + 1
        upper = interval[1]

print(fresh)
