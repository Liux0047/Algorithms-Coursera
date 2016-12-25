from operator import itemgetter

with open("data/jobs.txt") as f:
    input = [tuple(map(int, x.strip('\n').split())) for x in f.readlines()[1:]]

jobs = [tuple([x - y]) + tuple([x, y]) for x, y in input]

total_time = 0
total_sum = 0
for diff, weight, time in (sorted(jobs, key=itemgetter(0, 1), reverse=True)):
    total_time += time
    total_sum += total_time * weight

print(total_sum)
# 69119377652

jobs = [tuple([x / y]) + tuple([x, y]) for x, y in input]
total_time = 0
total_sum = 0
for diff, weight, time in (sorted(jobs, key=itemgetter(0), reverse=True)):
    total_time += time
    total_sum += total_time * weight
print(total_sum)
# 67311454237


