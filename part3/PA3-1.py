import heapq
from itertools import count

# read input
with open("data/huffman.txt") as f:
    contents = f.readlines()
    data = list(zip((int(x) for x in contents), count(0, 0)))
size = data[0][1]
del data[0]

heapq.heapify(data)

while len(data) > 1:
    item1 = heapq.heappop(data)
    item2 = heapq.heappop(data)
    # new_entry = (item1[0] + item2[0], max(item1[1] + 1, item2[1] + 1))
    new_entry = (item1[0] + item2[0], min(item1[1] + 1, item2[1] + 1))
    heapq.heappush(data, new_entry)

print(data)
# max 19
# min 9