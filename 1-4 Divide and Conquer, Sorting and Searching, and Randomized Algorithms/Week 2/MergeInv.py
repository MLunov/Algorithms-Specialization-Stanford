from datetime import datetime

start_time = datetime.now()


def mergeSort(myList, inv):
    n = len(myList)
    # print(n)
    if n == 1:
        return myList, inv
    a = mergeSort(myList[:int(n / 2)], inv)
    # print(a)
    b = mergeSort(myList[int(n / 2):], inv)
    # print(b)
    i, j, c, inv = 0, 0, [], a[1] + b[1]
    # print('a', a, 'b', b,'n: ', n)
    for k in range(n):
        if a[0][i] <= b[0][j]:
            c.append(a[0][i])
            i += 1
            if i == int(len(a[0])):
                c.extend(b[0][j:])
                return c, inv
        else:
            c.append(b[0][j])
            j += 1
            inv += int(n / 2) - i
            if j == int(len(b[0])):
                c.extend(a[0][i:])
                return c, inv


# myList = [8, 3, 2, 5, 4, 0, 10, 6]

with open('IntegerArray.txt') as f:
    array = list(map(int, f.read().split()))

# print(array[:10])
# answer = mergeSort(array[:10], 0)
# print(answer[0][:10], '\n', answer[1])

answer = mergeSort(array, 0)
print(answer[1])

### right answer is 2407905288

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

# Duration: 0:00:02.138204
