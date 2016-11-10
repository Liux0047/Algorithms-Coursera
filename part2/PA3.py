import bisect

a = []
with open("data/Median.txt") as f:
    input = [int(x.strip('\n')) for x in f.readlines()]

median_sum = 0
for x in input:
    bisect.insort(a, x)
    median_sum += a[int((len(a) - 1) / 2)]

print(median_sum % 10000)


# answer: 1213
