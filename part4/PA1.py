import array
import sys

# read input
with open("data/g3.txt") as f:
    data = [tuple(map(int, x.split())) for x in f.readlines()]
    vertex_count, edge_count = data[0]
    del data[0]
print("g3")

# init A
A = [[9999 for i in range(vertex_count)] for y in range(vertex_count)]
for i in range(vertex_count):
    A[i][i] = 0
for d in data:
    A[d[0] - 1][d[1] - 1] = d[2]

# run Floyd-Warshall algo
for k in range(vertex_count):
    for i in range(vertex_count):
        for j in range(vertex_count):
            A[i][j] = min(A[i][j], A[i][k] + A[k][j])
    print(k)

print("smallest:")
print(min([min(x) for x in A]))

# check for negative cycle
for i in range(vertex_count):
    if A[i][i] < 0:
        print("Negative cycle")
        break
else:
    print("No negative cycle")

# answers: g1=negative, g2=negative, g3=-19
