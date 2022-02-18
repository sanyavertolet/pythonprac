import os
import sys
import zlib

git_path = '.git'
objects_path = os.path.join(git_path, 'objects')
heads_path = os.path.join(git_path, 'refs', 'heads')

def print_branches():
    branches = os.listdir(heads_path)
    for branch in branches:
        print(branch)

def print_last_commit(branch_name):
    branch_head_path = os.path.join(heads_path, branch_name)
    try:
        with open(branch_head_path) as branch_head_file:
            commit_id = branch_head_file.readline().strip()
    except FileNotFoundError:
        print('No such brunch is found in this repo.')
        return
    commit_path = os.path.join(objects_path, commit_id[:2], commit_id[2:])
    with open(commit_path, 'rb') as commit_file:
        commit = zlib.decompress(commit_file.read())
        header, _, body = commit.partition(b'\x00')
        _, size = header.split()
        print(f'Last commit in branch \'{branch_name}\' with size {int(size)}\n')
        print(body.decode())

if len(sys.argv) == 1:
    print_branches()
elif len(sys.argv) == 2:
    print_last_commit(sys.argv[1])
else:
    print('Usage: python3 gitter')
