# read input
with open("data/mwis.txt") as f:
    data = [int(x) for x in f.readlines()]
size = data[0]

A = [0 for x in range(size + 1)]
A[1] = data[1]
for i in range(2, size + 1):
    A[i] = max(A[i - 1], A[i - 2] + data[i])

print(A[size])

i = size
selected = [0 for x in range(size)]
while i > 1:
    if A[i] == A[i - 1]:
        i -= 1
    else:
        selected[i - 1] = 1
        i -= 2
        if i == 1:
            selected[0] = 1

entries = [1, 2, 3, 4, 17, 117, 517, 997]
for x in entries:
    print(selected[x - 1], end="")
