import math
from itertools import combinations

# read and parse data
with open("day8.txt", "r") as f:
    points = [list(map(int, line.split(","))) for line in f.read().splitlines()]

# calculate and sort all the distances
dist = {(tuple(a), tuple(b)): math.dist(a, b) for a, b in combinations(points, 2)}
sorted_dist = dict(sorted(dist.items(), key=lambda item: item[1], reverse=True))

# initialize
circuts = [{tuple(p)} for p in points]

# merge circuts until there is only one left
while len(circuts) > 1:
    point = sorted_dist.popitem()[0]
    # count number of intersecting circuts
    intersection = [c for c in circuts if set(point) & c]
    if len(intersection) == 2:
        # We need to join two circuts
        circuts.append(intersection[0] | intersection[1])
        circuts.remove(intersection[0])
        circuts.remove(intersection[1])

print(point[0][0] * point[1][0])
