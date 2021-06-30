a, b, c = int(input()), int(input()), int(input())
def triangle(a, b, c):
    sides = [a, b, c]
    sort_sides = sorted(sides)
    if sort_sides[0] + sort_sides[1] > sort_sides[2]:
        return 'YES'
    return 'NO'
print(triangle(a, b, c))