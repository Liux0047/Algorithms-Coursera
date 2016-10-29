# This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.
#
# Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith entry of an array.
#
# Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.


def merge_sort(a, start, end):
    if end <= start:
        return
    mid = int((start + end) / 2)
    merge_sort(a, start, mid)
    merge_sort(a, mid + 1, end)
    merge(a, start, mid, end)


def merge(a, start, mid, end):
    global inversions
    left = a[start:mid + 1]
    right = a[mid + 1:end + 1]
    i = j = 0
    for k in range(start, end + 1):
        if i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
                inversions += len(left) - i
        elif i == len(left):
            a[k:end + 1] = right[j:]
            break
        else:
            a[k:end + 1] = left[i:]
            break


# read input
with open("data/IntegerArray.txt") as f:
    in_data = [int(x) for x in f.readlines()]
inversions = 0
merge_sort(in_data, 0, len(in_data) - 1)
print(inversions)

# answer: 2407905288
