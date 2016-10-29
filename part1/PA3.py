# Your task is to compute the total number of comparisons used to sort the given input file by QuickSort.
# As you know, the number of comparisons depends on which elements are chosen as pivots,
# so we'll ask you to explore three different pivoting rules.


def quick_sort(a, start, end):
    global comparisons
    if end <= start:
        return
    # pivot_pos = start
    # pivot_pos = end
    pivot_pos = get_mean_of_three(a, start, end)
    m = partition(a, start, end, pivot_pos)
    comparisons += end - start
    quick_sort(a, start, m - 1)
    quick_sort(a, m + 1, end)


def partition(a, start, end, pivot_pos):
    pivot = a[pivot_pos]
    if pivot != start:
        a[start], a[pivot_pos] = a[pivot_pos], a[start]
    j = start + 1
    for i in range(start + 1, end + 1):
        if a[i] < pivot:
            a[i], a[j] = a[j], a[i]
            j += 1
    a[start], a[j - 1] = a[j - 1], a[start]
    return j - 1


def get_mean_of_three(a, start, end):
    mid = int((start + end) / 2)
    li = [(a[start], start), (a[mid], mid), (a[end], end)]
    li.sort()
    return li[1][1]


# read input
with open("data/QuickSort.txt") as f:
    in_data = [int(x) for x in f.readlines()]
comparisons = 0
quick_sort(in_data, 0, len(in_data) - 1)
print(in_data)
print(comparisons)

# answer: 162085; 164123; 138382