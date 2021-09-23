n = int(input())

if n % 2 == 0 and n % 25 == 0:
    print('A + B - ', end='')
elif n % 25 == 0:
    print('A - B + ', end='')
else:
    print('A - B - ', end='')
if n % 8 == 0:
    print('C +')
else:
    print('C -')
