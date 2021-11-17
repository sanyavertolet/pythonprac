def Bisect(item, seq):
    if len(seq) == 0:
        return False
    middle = len(seq) // 2
    if(item == seq[middle]):
        return True
    if(item < seq[middle]):
        return Bisect(item, seq[:middle])
    return Bisect(item, seq[middle + 1:])

import sys
eval(sys.stdin.read())
