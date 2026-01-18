import numpy as np

file1 = open("day8.txt", "r")
points = []
for line in file1.readlines():
    point = list(map(int, line.strip().split(",")))
    points.append(point)

dist = {}
for a in points:
    for b in points:
        if a == b:
            pass
        elif (tuple(b), tuple(a)) in dist:
            pass
        else:
            dist[(tuple(a), tuple(b))] = np.sqrt(
                (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2
            )

sorted_dist = dict(sorted(dist.items(), key=lambda item: item[1], reverse=True))
circuts = [{tuple(p)} for p in points]

while len(circuts) > 1:
    numbers = sorted_dist.popitem()[0]
    inersection = []
    # count number of intersecting circuts
    for j in range(len(circuts)):
        if set.intersection(set(numbers), circuts[j]):
            inersection.append(circuts[j])
    if len(inersection) == 2:
        # We need to join two circuts
        circuts.append(set.union(inersection[0], inersection[1]))
        circuts.remove(inersection[0])
        circuts.remove(inersection[1])

wall_dist = numbers[0][0] * numbers[1][0]
print(wall_dist)
