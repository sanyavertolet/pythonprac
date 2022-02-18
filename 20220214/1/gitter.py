import os
import sys

heads_path = os.path.join('.git', 'refs', 'heads')

def print_branches():
    branches = os.listdir(heads_path)
    for branch in branches:
        print(branch)

if len(sys.argv) == 1:
    print_branches()
else:
    print('Usage: python3 gitter')
