def SUB(a, b):
    if '__sub__' in dir(a):
        return a - b
    return type(a)([item for item in a if item not in b]) if type(a) != type('') else ''.join([item for item in a if item not in b])


import sys
eval(sys.stdin.read())
