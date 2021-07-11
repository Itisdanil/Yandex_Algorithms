array = list(map(int, input().split()))
def more_neighbors(array):
    k = 0
    for i in range(1, len(array)-1):
        if array[i-1] < array[i] and array[i] > array[i+1]:
            k += 1
    return k
print(more_neighbors(array))