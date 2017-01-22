import math

# read input
with open("data/nn.txt") as f:
    points = [tuple(map(float, line.strip("\n").split()[1:])) for line in f.readlines()[1:]]

origin = current = points[0]
total_dist = 0

while len(points) > 0:
    min_dist_sq = (0, math.inf)
    for idx, p in enumerate(points):
        dist_sq = math.pow(current[0] - p[0], 2) + math.pow(current[1] - p[1], 2)
        if dist_sq < min_dist_sq[1]:
            min_dist_sq = (idx, dist_sq)
    current = points[min_dist_sq[0]]
    total_dist += math.sqrt(min_dist_sq[1])
    points.pop(min_dist_sq[0])
    print(len(points))

total_dist += math.sqrt(math.pow(current[0] - origin[0], 2) + math.pow(current[1] - origin[1], 2))
print(total_dist)

# answer: 1203406
