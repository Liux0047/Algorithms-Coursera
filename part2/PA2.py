class Vertex:
    def __init__(self, id):
        self.id = id
        self.out_edges = []
        self.key = 1000000

    def add_edge(self, edge):
        self.out_edges.append(edge)


class Edge:
    def __init__(self, head, tail, length):
        self.head = head
        self.tail = tail
        self.length = length


# construct graph
with open("data/dijkstraData.txt") as f:
    content = f.readlines()
    content = [x.strip('\n') for x in content]
    vertex_count = len(content)
    vertices = [Vertex(i) for i in range(1, vertex_count + 1)]
    edges = []

    for line in content:
        line_entries = line.split()
        tail = vertices[int(line_entries[0]) - 1]
        for head, length in (l.split(',') for l in line_entries[1:]):
            e = Edge(vertices[int(head) - 1], tail, int(length))
            tail.add_edge(e)
            edges.append(e)

processed = []
remainder = [v for v in vertices]
vertices[0].key = 0
while len(remainder):
    w = min(remainder, key=lambda v: v.key)
    remainder.remove(w)
    for e in w.out_edges:
        if w.key + e.length < e.head.key:
            e.head.key = w.key + e.length

output_vertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
for vi in output_vertices:
    print(vertices[vi - 1].key)


# answer:2599,2610,2947,2052,2367,2399,2029,2442,2505,3068
