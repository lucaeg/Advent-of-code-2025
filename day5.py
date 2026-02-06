intervals = []
numbers = []

# read and parse data
with open("day5.txt", "r") as f:
    for line in f.read().splitlines():
        if not line:
            continue
        try:
            numbers.append(int(line))
        except ValueError:
            intervals.append(list(map(int, line.split("-"))))

intervals.sort()

# Initial case
lower_bound = intervals[0][0]
upper_bound = intervals[0][1]
total_numbers = intervals[0][1] - intervals[0][0] + 1

# find total amount of numbers covered by the intervals
for interval in intervals[1:]:
    if interval[0] <= upper_bound:
        if interval[1] <= upper_bound:
            continue
        else:
            total_numbers += interval[1] - upper_bound
            upper_bound = interval[1]
    else:
        total_numbers += interval[1] - interval[0] + 1
        upper_bound = interval[1]

print(total_numbers)
