def func(array):
    k = 0
    for i in range(1, len(array)):
        if array[i-1] < array[i]:
            k += 1
    if k == len(array) - 1:
        return 'YES'
    return 'NO'
print(func(list(map(int, input().split()))))