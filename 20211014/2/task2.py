from math import sin

def scale(A, B, a, b, x):
    return (x - A) / (B - A) * (b - a) + a

f = sin

width = 80
height = 25

x_from, x_to = -4, 4
y_from, y_to = -1, 1

X = [scale(0, width + 1, x_from, x_to, x) for x in range(width + 1)]
Y = [f(x) for x in X]

min_y, max_y = min(Y), max(Y)

for y in Y:
    print(int(scale(min_y, max_y, 0, width, y)) * " " + "*")
