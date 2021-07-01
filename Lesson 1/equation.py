a, b, c = int(input()), int(input()), int(input())
def equation(a, b, c):
    if c < 0 or (a == 0 and (b != 0 or c != 0) and c**2 != b) or (a != 0 and (c**2 - b) % a != 0):
        return 'NO SOLUTION'
    elif (a == 0 and b == 0 and c == 0) or (a == 0 and c**2 == b):
        return 'MANY SOLUTIONS'
    return int((c**2 - b) / a)
print(equation(a, b, c))