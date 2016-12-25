from collections import namedtuple
from operator import itemgetter, attrgetter
from part3.vheap import Vheap


class Vertex:
    def __init__(self, vid, min_cost):
        self.vid = vid
        self.edges = []
        self.pos = None
        self.min_cost = min_cost


Edge = namedtuple('Edge', 'v1 v2 cost')


def ud_combo(e, v):
    if e.cost < v.min_cost:
        remains.delete(v)
        v.min_cost = e.cost
        remains.push(v)


with open("data/edges.txt") as f:
    data = [tuple(map(int, x.strip('\n').split())) for x in f.readlines()]
    vertex_count, edge_count = data[0]
    del data[0]

*_, max_cost = max(data, key=itemgetter(2))
vertices = [Vertex(i, max_cost + 1) for i in range(1, vertex_count + 1)]
for item in data:
    v1, v2, cost = item
    e = Edge(vertices[v1 - 1], vertices[v2 - 1], cost)
    vertices[item[0] - 1].edges.append(e)
    vertices[item[1] - 1].edges.append(e)

for e in vertices[0].edges:
    e.v2.min_cost = e.cost
    e.v1.min_cost = e.cost
del vertices[0]

remains = Vheap(attrgetter('min_cost'))
for v in vertices:
    remains.push(v)

total_cost = 0
total_cost_e = 0
while len(remains):
    v = remains.pop()
    total_cost += v.min_cost
    for e in v.edges:
        if e.v1 in remains:
            ud_combo(e, e.v1)
        elif e.v2 in remains:
            ud_combo(e, e.v2)

print(total_cost)
# -3612829