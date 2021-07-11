array = list(map(int, input().split()))
def findmax2(array):
    max1, max2, max3, max4 = max(array[0], array[1]), min(array[0], array[1]), max(array[0], array[1]), min(array[0], array[1])
    for i in range(2, len(array)):
        if array[i] > max1:
            max2 = max1
            max1 = array[i]
        elif array[i] > max2:
            max2 = array[i]
    for i in range(2, len(array)):
        if array[i] < max4:
            max3 = max4
            max4 = array[i]
        elif array[i] < max3:
            max3 = array[i]
    if max1 * max2 > max3 * max4:
        return (min(max1, max2), max(max1, max2))
    return (min(max3, max4), max(max3, max4))
print(findmax2(array))