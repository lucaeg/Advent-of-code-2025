from functools import cache

# read and parse data
with open("day9.txt", "r") as f:
    points = [tuple(map(int, line.split(","))) for line in f.read().splitlines()]

# create edges and group them
edges = list(zip(points, points[1:] + points[:1]))
horizontal_edges = [
    (a, b) if a[0] <= b[0] else (b, a) for a, b in edges if a[1] == b[1]
]
vertical_edges = [(a, b) if a[1] <= b[1] else (b, a) for a, b in edges if a[0] == b[0]]


# Function to check if vertical ray from p upwards
# intersects a horizontal edge.
def ray_intersects_edge(p, edge):
    a, b = edge

    in_between = a[0] <= p[0] < b[0]
    over = a[1] < p[1]
    return over and in_between


def point_on_edge(p):
    for a, b in horizontal_edges:
        if p[1] == a[1] and a[0] <= p[0] <= b[0]:
            return True
    for a, b in vertical_edges:
        if p[0] == a[0] and a[1] <= p[1] <= b[1]:
            return True
    return False


# function to check if a point is in the orthogonal hull
# of the horizontal and vertical edges, we use the ray
# casting algorithm to determine membership
@cache
def in_hull(p):
    if point_on_edge(p):
        return True
    return sum(ray_intersects_edge(p, e) for e in horizontal_edges) % 2 == 1


# function to check if boundary of a rectangle is fully
# contained in the orthogonal hull
def check_boundary(a, b):
    for p in range(a[0], b[0] + 1):
        if not in_hull((p, a[1])):
            return False

    for p in range(a[0], b[0] + 1):
        if not in_hull((p, b[1])):
            return False

    y_start = min(a[1], b[1])
    y_end = max(a[1], b[1])

    for p in range(y_start, y_end + 1):
        if not in_hull((a[0], p)):
            return False

    for p in range(y_start, y_end + 1):
        if not in_hull((b[0], p)):
            return False

    return True


# iterate over corners to find
# largest rectangle in the orthogonal hull
area = 0
counter = 0
for a in points:
    for b in points:
        if a[0] < b[0]:
            # Stopping criterion
            if not (in_hull((a[0], b[1])) and in_hull((b[0], a[1]))):
                continue
            if check_boundary(a, b):
                area = max(area, (b[0] - a[0] + 1) * (a[1] - b[1] + 1))

print(area)
