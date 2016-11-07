# Kosaraju’s Two-­‐Pass Algorithm to compute
# Strongly connected components

from collections import Counter


class Vertex:
    def __init__(self, vid):
        self.vid = vid
        self.out_edges = []
        self.in_edges = []
        self.explored = False

    def add_out_edge(self, edge):
        self.out_edges.append(edge)

    def add_in_edge(self, edge):
        self.in_edges.append(edge)


class Edge:
    def __init__(self, tail, head):
        self.head = head
        self.tail = tail


# construct the graph
with open("data/SCC.txt") as f:
    content = f.readlines()
    content = [x.strip('\n') for x in content]
    vertex_count = len(content)
    edges = []
    vertices = [Vertex(i) for i in range(1, vertex_count + 1)]

    for line in content:
        entry = [int(x) for x in line.split()]
        if entry[0] != entry[1]:
            edge = Edge(vertices[entry[0] - 1], vertices[entry[1] - 1])
            edges.append(edge)
            vertices[entry[0] - 1].out_edges.append(edge)
            vertices[entry[1] - 1].in_edges.append(edge)

# DFS loop
finishing_time = 0
vertices_ft = [None] * vertex_count
leader = None


def DFS(root, is_rev):
    DFS_stack = []
    poped_list = []
    DFS_stack.append(root)
    root.explored = True
    while len(DFS_stack):
        vertex = DFS_stack.pop()
        if is_rev:
            poped_list.append(vertex)
            for each_edge in vertex.in_edges:
                if not each_edge.tail.explored:
                    DFS_stack.append(each_edge.tail)
                    each_edge.tail.explored = True
        else:
            vertex.leader = leader
            for each_edge in vertex.out_edges:
                if not each_edge.head.explored:
                    DFS_stack.append(each_edge.head)
                    each_edge.head.explored = True

    while len(poped_list):
        vertex = poped_list.pop()
        global finishing_time, vertices_ft
        vertices_ft[finishing_time] = vertex
        vertex.ft = finishing_time
        finishing_time += 1


for v in reversed(vertices):
    if not v.explored:
        DFS(v, True)

for v in vertices:
    v.explored = False

for v in reversed(vertices_ft):
    if not v.explored:
        leader = v.vid
        DFS(v, False)

result = Counter()
for v in vertices:
    result[v.leader] += 1

# Output the vertex count in the largest 5 SCCs
print([r for v, r in result.most_common(5)])
# answer: 434821,968,459,313,211
