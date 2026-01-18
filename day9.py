from functools import cache

file1 = open("day9.txt", "r")
points = [tuple(map(int, line.strip().split(","))) for line in file1]
edges = list(zip(points, points[1:] + points[:1]))
horizontal_edges = [
    (x, y) if x[0] <= y[0] else (y, x) for x, y in edges if x[1] == y[1]
]
vertical_edges = [(x, y) if x[1] <= y[1] else (y, x) for x, y in edges if x[0] == y[0]]


def ray_intersect_edge(p, edge):
    """Algorithm  to check if vertical ray from p upwards
    intersects a horizontal edge."""
    x, y = edge

    in_between = x[0] <= p[0] < y[0]
    over = x[1] < p[1]
    return over and in_between


def point_on_edge(p):
    for x, y in horizontal_edges:
        if p[1] == x[1] and x[0] <= p[0] <= y[0]:
            return True
    for x, y in vertical_edges:
        if p[0] == x[0] and x[1] <= p[1] <= y[1]:
            return True
    return False


@cache
def in_hull(p):
    if point_on_edge(p):
        return True
    return sum(ray_intersect_edge(p, e) for e in horizontal_edges) % 2 == 1


area = 0
counter = 0
for a in points:
    print("counter = ", counter)
    counter += 1
    for b in points:
        if a[0] < b[0]:
            # Stopping criterion
            if not (in_hull((a[0], b[1])) and in_hull((b[0], a[1]))):
                continue
            lower_boundary = [in_hull((p, a[1])) for p in range(a[0], b[0] + 1)]
            upper_boundary = [in_hull((p, b[1])) for p in range(a[0], b[0] + 1)]
            if a[1] < b[1]:
                left_boundary = [in_hull((a[0], p)) for p in range(a[1], b[1] + 1)]
                right_boundary = [in_hull((b[0], p)) for p in range(a[1], b[1] + 1)]
                boundary = (
                    lower_boundary + upper_boundary + left_boundary + right_boundary
                )
                if all(boundary):
                    area = max(area, (b[0] - a[0] + 1) * (b[1] - a[1] + 1))
            elif b[1] < a[1]:
                left_boundary = [in_hull((a[0], p)) for p in range(b[1], a[1] + 1)]
                right_boundary = [in_hull((b[0], p)) for p in range(b[1], a[1] + 1)]
                boundary = (
                    lower_boundary + upper_boundary + left_boundary + right_boundary
                )
                if all(boundary):
                    area = max(area, (b[0] - a[0] + 1) * (a[1] - b[1] + 1))

print(area)
