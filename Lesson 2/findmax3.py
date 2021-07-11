array = list(map(int, input().split()))
def findmax3(array):
    array = sorted(array)
    if array[0] * array[1] * array[-1] > array[-1] * array[-2] * array[-3]:
        return (array[0], array[1], array[-1])
    return (array[-1], array[-2], array[-3])
print(findmax3(array))