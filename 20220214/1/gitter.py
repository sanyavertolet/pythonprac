import os

def print_branches():
    branches = os.listdir('.git/refs/heads/')
    for branch in branches:
        print(branch)


if len(sys.argv) == 1:
    print_branches()
else:
    print('Usage: python3 gitter')
