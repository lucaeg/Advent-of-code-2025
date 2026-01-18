import textwrap
from itertools import groupby

file1 = open("day2.txt", "r")
line = file1.readline()

ranges = line.split(",")


def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def is_invalid(id):
    if len(id) % 2 == 1:
        half_length = int((len(id) - 1) / 2)
    half_length = int(len(id) / 2)

    for i in range(1, half_length + 1):
        if len(id) % i == 0:
            numbers = textwrap.wrap(id, i)
            if all_equal(numbers):
                return False
    return True


counter = 0
for interval in ranges:
    bounds = list(map(int, interval.split("-")))
    for id in range(bounds[0], bounds[1] + 1):
        if not is_invalid(str(id)):
            counter += id

print(counter)
