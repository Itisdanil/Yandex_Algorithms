tr, tc = map(int,input().split())
mode = input()
def conditioner(tr, tc, mode):
    for i in range(4):
        if mode == 'freeze':
            if tr <= tc:
                return tr
            return tc
        elif mode == 'heat':
            if tr >= tc:
                return tr
            return tc
        elif mode == 'auto':
            return tc
        elif mode == 'fan':
            return tr
print(conditioner(tr, tc, mode))