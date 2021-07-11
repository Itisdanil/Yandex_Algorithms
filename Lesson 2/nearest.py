n = int(input())
array = list(map(int, input().split()[:n]))
x = int(input())
def nearest(n, array, x):
    minimum = abs(array[0] - x)
    num = array[0]
    for i in range(1, len(array)):
        if abs(array[i] - x) <= minimum:
            minimum = abs(array[i] - x)
            num = array[i]
    return num
print(nearest(n, array, x))