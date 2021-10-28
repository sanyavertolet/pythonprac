def fib(m, n):
    prev, preprev = 1, 0
    if m == 0:
        yield 1
    for i in range(1, n):
        prev, preprev = prev + preprev, prev
        if i >= m:
            yield prev


import sys
exec(sys.stdin.read())

