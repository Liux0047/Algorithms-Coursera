import sys

# read input
with open("data/knapsack1.txt") as f:
    data = [tuple(map(int, x.split())) for x in f.readlines()]
    knapsack_size = data[0][0]
    num_items = data[0][1]
#
# A = [[0 for x in range(knapsack_size + 1)] for y in range(num_items + 1)]
# for i in range(1, num_items + 1):
#     for w in range(knapsack_size + 1):
#         if w - data[i][1] >= 0:
#             A[i][w] = max(A[i - 1][w], A[i - 1][w - data[i][1]] + data[i][0])
#         else:
#             A[i][w] = A[i - 1][w]
# print(A[num_items][knapsack_size])


# answer: 2493893


sys.setrecursionlimit(1000000)

D = {}


def recur(i, w):
    if i == 0:
        D[(i, w)] = 0
        return

    if (i - 1, w) not in D:
        recur(i - 1, w)
    p1 = D[(i - 1, w)]

    if w - data[i][1] >= 0:
        if (i - 1, w - data[i][1]) not in D:
            recur(i - 1, w - data[i][1])
        p2 = D[(i - 1, w - data[i][1])]
        D[(i, w)] = max(p1, p2 + data[i][0])
    else:
        D[(i, w)] = p1


recur(num_items, knapsack_size)
print(D[num_items, knapsack_size])

# answer: 4243395
