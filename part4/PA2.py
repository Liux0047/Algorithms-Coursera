import math
from collections import deque, defaultdict


# generate all permutations for given len
def gen_perm(s, len, perms, size_left):
    s = deque(s)
    if len == 1:
        if size_left == 0:
            perms.append(tuple(s))
        elif size_left == 1:
            s.appendleft(len)
            perms.append(tuple(s))
    else:
        gen_perm(s, len - 1, perms, size_left)
        if size_left > 0:
            s.appendleft(len)
            gen_perm(s, len - 1, perms, size_left - 1)


# read input
with open("data/tsp.txt") as f:
    data = [tuple(map(float, line.strip("\n").split())) for line in f.readlines()[1:]]
size = len(data)

distances = [[math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2)) for p1 in data] for p2 in data]

# base case
A = defaultdict(lambda: math.inf)
A[(), 0] = 0

max_set = ()
for m in range(1, size):
    print('m = ' + str(m))
    permutations = []
    gen_perm(deque(), size - 1, permutations, m)
    if m == size - 1:
        max_set = permutations[0]
    for set_m in permutations:
        for j in set_m:
            min_dist = math.inf
            prev_set = tuple(x for x in set_m if x != j)
            for k in (0,) + set_m:
                if k != j:
                    result = A[prev_set, k] + distances[k][j]
                    if result < min_dist:
                        min_dist = result
            A[set_m, j] = min_dist

min_total = math.inf
for j in range(1, size):
    result = A[max_set, j] + distances[j][0]
    if result < min_total:
        min_total = result

print(min_total)
# answer: 26442
