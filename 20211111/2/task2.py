import math
class InvalidException(Exception): pass


class BadTriangle(Exception): pass


def TriangleSquare(string):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(string)
    except:
        raise InvalidException
    a, b, c = math.dist((x1, y1), (x2, y2)), math.dist((x3, y3), (x2, y2)), math.dist((x1, y1), (x3, y3))
    p = (a + b + c) / 2
    square = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    if not square:
        raise BadTriangle
    return square


while True:
    try:
        print("%.2f" % TriangleSquare(input()))
    except BadTriangle:
        print('Not a triangle')
    except (InvalidException, KeyboardInterrupt, EOFError):
        print('Invalid input')
    else:
        break
