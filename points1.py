import math as m

### distance functions
def distance(p1, p2):
    return m.sqrt(m.pow(p2.x - p1.x, 2) + m.pow(p2.y - p1.y, 2))


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.min_radius = 0
        self.neighbors = []
        self.count_neighbors = 0

    def __repr__(self):
        return "\n Point: (x=%s, y=%s, min_radius=%s, count_neighbors=%s)" % (self.x, self.y, self.min_radius,
                                                                                         self.count_neighbors)


"""
points.txt should look like:
1 2
5 6
2 3
2 3
6 5
...
"""

all_points = []
with open('points.txt') as _points:
    for _point in _points:
        _point = _point.split()
        _point = [int(coordinate) for coordinate in _point]
        all_points.append(_point)

all_points = [p for i,p in enumerate(all_points) if p not in all_points[:i]]


points = []

for p in all_points:
    points.append(Point(p[0], p[1]))

min_radius = float('inf')

for p1 in points:
    for p2 in points:
        if (p1!=p2):
            dist = distance(p1, p2)
            if dist<min_radius:
                min_radius = dist
    p1.min_radius = min_radius
    min_radius = float('inf')

for p1 in points:
    for p2 in points:
        if (p1!=p2):
            if distance(p1, p2)<=2*p1.min_radius:
                p1.neighbors.append(p2)
    p1.count_neighbors = len(p1.neighbors)

print points
