from math import *

def scale(A, B, a, b, x):
    return (x - A) / (B - A) * (b - a) + a

def function(s):
    def f(x):
        return eval(s)
    return f

data = input().split()

width, height = int(data[0]), int(data[1])
x_from, x_to = float(data[2]), float(data[3])
s = ''.join(data[4:])
f = function(s)
X = [(x, scale(0, width + 1, x_from, x_to, x)) for x in range(width + 1)]
F = [(x[0], f(x[1])) for x in X]

y_from = F[0][1]
y_to = F[0][1]

for y in F:
    if y[1] > y_to:
        y_to = y[1]
    if y[1] < y_from:
        y_from = y[1]

F = [(y[0], round(scale(y_to, y_from, 0, height + 1, y[1]))) for y in F]

field = [[' ' for j in range(width + 2)] for i in range(height + 2)]


for i in range(len(F)):
    field[F[i][1]][F[i][0]] = '*'
    if i != 0:
        prev_point = F[i - 1]
        for j in range(min(F[i - 1][1], F[i][1]) + 1, max(F[i - 1][1], F[i][1])):
            field[j][F[i - 1][0]] = '*'


field = [''.join(raw) for raw in field]

for raw in field:
    print(raw)

#print(*field)
