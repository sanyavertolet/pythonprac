a = []
a.append(eval(input()))
n = len(a[0])
for i in range(1, n):
    a.append(eval(input()))
b = [eval(input()) for i in range(n)]

c = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            c[i][j] += a[i][k] * b[k][j]
for lines in c:
    print(lines)
