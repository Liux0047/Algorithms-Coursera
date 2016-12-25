from collections import deque

data = {}

# BITS = 5
BITS = 24

# read input
with open("data/clustering_big.txt") as f:
    for x in f.readlines()[1:]:
        data[int(x.replace(' ', ''), 2)] = False

# construct mask patterns
patterns = []
for i in range(BITS):
    str = '0' * i + '1' + '0' * (BITS - 1 - i)
    patterns.append(int(str, 2))

for i in range(BITS - 1):
    for j in range(i + 1, BITS):
        str = '0' * i + '1' + '0' * (j - i - 1) + '1' + '0' * (BITS - j - 1)
        patterns.append(int(str, 2))

# main loop
cluster_count = 0
while data:
    start_node = next(iter(data))
    q = deque([start_node])
    data[start_node] = True
    cluster = []
    while len(q):
        node = q.popleft()
        for p in patterns:
            candidate = node ^ p
            if candidate in data and not data[candidate]:
                data[candidate] = True
                cluster.append(candidate)
                q.append(candidate)
    del data[start_node]
    for n in cluster:
        del data[n]
    cluster_count += 1
    print(len(data))

print(cluster_count)


# answer: 6118
