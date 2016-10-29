# Your task is to code up and run the randomized contraction algorithm for the min cut problem and
# use it on the above graph to compute the min cut.
from collections import namedtuple
import random


class Vertex:
    def __init__(self, id):
        self.id = id
        self.edges = []


class Edge:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail


def contract(vertices, edges):
    while len(vertices) > 2:
        e = random.choice(edges)
        for e_out in e.head.edges:
            if e_out.head != e.tail:
                e_out.tail = e.tail
                for e_in in e_out.head.edges:
                    if e_in.head == e.head:
                        e_in.head = e.tail
                e.tail.edges.append(e_out)
            else:
                edges.remove(e_out)

        to_removes = []
        for e_parallel in e.tail.edges:
            if e_parallel.head == e.head:
                edges.remove(e_parallel)
                to_removes.append(e_parallel)
        for e_to_remove in to_removes:
            e.tail.edges.remove(e_to_remove)

        vertices.remove(e.head)

    return len(edges) / 2


def construct():
    vertices = []
    edges = []

    # read input and construct graph
    with open("data/kargerMinCut.txt") as f:
        lines = f.readlines()
        for i in range(1, len(lines) + 1):
            vertices.append(Vertex(i))
        for line in lines:
            entries = line.split()
            tail = vertices[int(entries[0]) - 1]
            for entry in map(int, entries[1:]):
                e = Edge(vertices[entry - 1], tail)
                edges.append(e)
                tail.edges.append(e)
    return vertices, edges


smallest = 99999
for i in range(40):
    v, e = construct()
    min_cut = contract(v, e)
    if min_cut < smallest:
        smallest = min_cut

print(smallest)
