from datetime import datetime

start_time = datetime.now()


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

# assignment 3.1: the right answer is 162085

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

# Duration: 0:00:00.080005


# #----------------------------------------------------------------------
# # for debugging
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
#     j = Partition(array, l, r)
#     # print('l:', l, ', j:', j, ', r:', r)
#     c += QuickSort(array, l, j, c)
#     if j + 1 >= r - 1:
#         return c
#     c += QuickSort(array, j + 1, r, c)
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
