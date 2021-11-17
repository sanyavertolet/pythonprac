import itertools

def slide(seq, n):
    seq = itertools.tee(iter(seq))
    while next(seq[1], None) is not None:
        yield from itertools.islice(seq[0], n)
        seq = itertools.tee(seq[1], n)


import sys
exec(sys.stdin.read())
