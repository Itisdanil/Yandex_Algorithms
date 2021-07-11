def type_seq():
    n, array = int(input()), []
    while n != -2000000000:
        array.append(n)
        n = int(input())
    if len(set(array)) == 1:
        return 'CONSTANT'
    a, b, c, d = 0, 0, 0, 0
    for i in range(1, len(array)):
        if array[i-1] < array[i]:
            a += 1
        if array[i-1] <= array[i]:
            b += 1
        if array[i-1] > array[i]:
            c += 1
        if array[i-1] >= array[i]:
            d += 1
    if a == len(array) - 1:
        return 'ASCENDING'
    elif b == len(array) - 1:
        return 'WEAKLY ASCENDING'
    elif c == len(array) - 1:
        return 'DESCENDING'
    elif d == len(array) - 1:
        return 'WEAKLY DESCENDING'
    return 'RANDOM'
print(type_seq())