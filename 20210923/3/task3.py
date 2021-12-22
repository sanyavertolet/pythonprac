n = int(input())
i = 0
while i < 3:
    j = 0
    while j < 3:
        a = (n + i) * (n + j)
        s = 0
        while a != 0:
            s += a % 10
            a //= 10
        if s == 6:
            print(n + i, '*', n + j, '=:=)', sep='', end=' ')
        else:
            print(n + i, '*', n + j, '=', (n + i) * (n + j), sep='', end=' ')
        j += 1
    i += 1
    print('')
