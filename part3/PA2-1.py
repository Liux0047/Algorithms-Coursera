from collections import namedtuple
from operator import itemgetter

K = 4


class Vertex:
    def __init__(self, id):
        self.id = id
        self.leader = self
        self.count = 1
        self.citizens = [self]


Edge = namedtuple('Edge', 'v1 v2 cost')


# merge leader 2 into leader 1
def merge(l1, l2):
    for v in l2.citizens:
        v.leader = l1.leader
    l1.count = l1.count + l2.count
    l1.citizens.extend(l2.citizens)


# read input
with open("data/clustering1.txt") as f:
    data = [tuple(map(int, x.strip('\n').split())) for x in f.readlines()]
    vertex_count = cluster_count = data[0][0]
    del data[0]

# init vertices
vertices = []
for i in range(1, vertex_count + 1):
    vertices.append(Vertex(i))

# init edges
edges = []
for element in data:
    v1, v2, cost = element
    edges.append(Edge(vertices[v1 - 1], vertices[v2 - 1], cost))

# sort the edges
edges.sort(key=itemgetter(2), reverse=True)

# main loop
while True:
    e = edges.pop()
    if e.v1.leader is not e.v2.leader:  # merge the two cluster
        if cluster_count == K:
            print(e.cost)
            break
        if e.v1.leader.count > e.v2.leader.count:
            merge(e.v1.leader, e.v2.leader)
        else:
            merge(e.v2.leader, e.v1.leader)
        cluster_count -= 1


# Answer: 106
