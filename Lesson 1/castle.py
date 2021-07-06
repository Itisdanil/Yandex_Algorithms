a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
window = [d, e]
size = [a, b, c]
def castle(window, size):
    window = sorted(window)
    size = sorted(size)
    if size[0] <= window[0] and size[1] <= window[1]:
        return 'YES'
    return 'NO'
print(castle(window, size))