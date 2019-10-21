from datetime import datetime

start_time = datetime.now()

import math


def Partition(array, l, r):
    i = l + 1
    for j in range(l + 1, r):
        if array[j] < array[l]:
            array[j], array[i] = array[i], array[j]
            i += 1
    if i != l + 1:
        array[l], array[i - 1] = array[i - 1], array[l]
    return i - 1


def QuickSort(array, l, r, c):
    if l + 1 >= r:
        return 0
    c = r - l - 1
    idx_mean = l + math.ceil((r - l) / 2) - 1
    idx_med = sorted([(array[l], l), (array[idx_mean], idx_mean), (array[r - 1], r - 1)])[1][1]
    if l != idx_med:
        array[l], array[idx_med] = array[idx_med], array[l]
    j = Partition(array, l, r)
    c += QuickSort(array, l, j, c)
    if j + 1 >= r - 1:
        return c
    c += QuickSort(array, j + 1, r, c)
    return c


# array = [3, 1, 2, 4, 5, 8, 7, 6, 9]

with open('QuickSort.txt') as f:
    array = list(map(int, f.read().split()))

c = 0
print(QuickSort(array, 0, len(array), c))
# print(array)

# assignment 3.3: the right answer is 138382

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

# Duration: 0:00:00.078000


# #----------------------------------------------------------------------
# # for debugging
#
#
# import math
#
#
# def Partition(array, l, r):
#     i = l + 1
#     for j in range(l + 1, r):
#         if array[j] < array[l]:
#             array[j], array[i] = array[i], array[j]
#             # print('in prePartition: ', array)
#             i += 1
#     if i != l + 1:
#         array[l], array[i - 1] = array[i - 1], array[l]
#     # print('in Partition: ', array)
#     return i - 1
#
#
# def QuickSort(array, l, r, c):
#     if l + 1 >= r:
#         return 0
#     c = r - l - 1
#     # print('l:', l, ', r:', r)
#     # print('print c:', c)
#     med = sorted([array[l], array[l + math.ceil((r - l) / 2) - 1], array[r - 1]])[1]
#     idx_med = array.index(med)
#     # print([array[l], array[l + math.ceil((r-l)/2) - 1], array[r - 1]])
#     # print(sorted([array[l], array[l + math.ceil((r-l)/2) - 1], array[r - 1]]))
#     # print('mediana:', med)
#     # print('index med:', idx_med)
#     # print(array[l], array[idx_med])
#     if l != idx_med:
#         array[l], array[idx_med] = array[idx_med], array[l]
#     # print(array[l], array[idx_med])
#     j = Partition(array, l, r)
#     # print('l:', l, ', j:', j, ', r:', r)
#     c += QuickSort(array, l, j, c)
#     # print('c1:', c)
#     if j + 1 >= r - 1:
#         return c
#     c += QuickSort(array, j + 1, r, c)
#     # print('c2:', c)
#     return c
#
#
# # array = [3, 1, 2, 4, 5, 8, 7, 6, 9]
#
# with open('QuickSort.txt') as f:
#     array = list(map(int, f.read().split()))
#
# # print(Partition(array, 0, len(array)))
# c = 0
# print(QuickSort(array, 0, len(array), c))
# # print(array)
#
# # Duration: 0:00:00.898052
