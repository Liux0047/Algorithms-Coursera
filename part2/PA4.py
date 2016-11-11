with open("data/2sum.txt") as f:
    input = set([int(x.strip('\n')) for x in f.readlines()])

count = 0
for twosum in range(-10000, 10001):
    print(twosum)
    for x in input:
        if (twosum - x) in input and twosum - x != x:
            count += 1
            break
print(count)
# answer: 427
