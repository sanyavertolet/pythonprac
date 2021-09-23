s = 0
while s <= 21:
    n = int(input())
    if n > 0:
        s += n
    else:
        print(n)
        break
else:
    print(s)
