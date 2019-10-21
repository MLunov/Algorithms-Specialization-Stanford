import timeit


# standart sort by Python
# def stdSort():
#     return sorted([8, 3, 2, 5, 1, 4, 10, 6])
#
# print(timeit.timeit("stdSort()", setup="from __main__ import stdSort", number=1))
# running time is 6.531000000004061e-06

# Merge Sort algorithm for even number of elements n:
def mergeSort():
    myList = [8, 3, 2, 5, 4, 1, 10, 6]
    n = len(myList)
    a = sorted(myList[:int(n / 2)])
    b = sorted(myList[int(n / 2):])
    i, j, c = 0, 0, []
    for k in range(len(myList)):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
            if i == int(n / 2):
                c.extend(b[j:])
                return c
        else:
            c.append(b[j])
            j += 1
            if j == int(n / 2):
                c.extend(a[i:])
                return c


print(timeit.timeit("mergeSort()", setup="from __main__ import mergeSort", number=1))
# running time is 3.592100000000126e-05
