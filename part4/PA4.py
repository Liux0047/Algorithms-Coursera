import sys

# read input
with open("data/2sat1.txt") as f:
    lines = f.readlines()
    size = int(lines[0])
    constraints = [tuple(map(int, x.split())) for x in lines[1:]]

X = [False] * size
assigned = [False] * size


def assign(index):
    # print(index)
    if index == len(constraints):
        return True

    s1, s2 = constraints[index]

    # note the sign and convert into index
    sign1 = sign2 = True
    if s1 < 0:
        sign1 = False
        s1 = -s1
    if s2 < 0:
        sign2 = False
        s2 = -s2
    s1 -= 1
    s2 -= 1

    # use == in place of xnor
    if assigned[s1] and assigned[s2]:
        if (X[s1] == sign1) or (X[s2] == sign2):
            return assign(index + 1)
        else:
            return False
    elif assigned[s1]:
        if X[s1] != sign1:
            assigned[s2] = True
            X[s2] = sign2
        if assign(index + 1):
            return True
        else:
            assigned[s2] = False
            return False
    elif assigned[s2]:
        if X[s2] != sign2:
            assigned[s1] = True
            X[s1] = sign1
        if assign(index + 1):
            return True
        else:
            assigned[s1] = False
            return False
    else:
        assigned[s1] = True
        X[s1] = sign1
        if not assign(index + 1):
            assigned[s1] = False
            assigned[s2] = True
            X[s2] = sign2
            if not assign(index + 1):
                assigned[s2] = False
                return False
        return True


sys.setrecursionlimit(len(constraints) * 2)
if assign(0):
    print('solution found')
else:
    print('No feasible solution')


# answer: 101100
