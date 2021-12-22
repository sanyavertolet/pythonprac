import math
class InvalidException(Exception): pass


class BadTriangle(Exception): pass


def TriangleSquare(string):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(string)
    except:
        raise InvalidException
    else:
        try:
            a, b, c = math.dist((x1, y1), (x2, y2)), math.dist((x3, y3), (x2, y2)), math.dist((x1, y1), (x3, y3))
        except:
            raise InvalidException
        else:
            p = (a + b + c) / 2
            square = (p * (p - a) * (p - b) * (p - c)) ** 0.5
            if not square:
                raise BadTriangle
            else:
                return square

import sys
while True:
    try:
        area = TriangleSquare(input())
    except BadTriangle:
        print('Not a triangle')
    except (InvalidException, Exception):
        print('Invalid input')
    else:
        print('%.2f' % area)
        break

