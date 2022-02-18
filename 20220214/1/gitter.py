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


def get_head_commit_id(branch_name):
    branch_head_path = os.path.join(heads_path, branch_name)
    try:
        with open(branch_head_path) as branch_head_file:
            return branch_head_file.read().strip()
    except FileNotFoundError as exception:
        print('No such brunch is found in this repo.')
        raise exception

def print_commit(commit_id):
    commit_path = os.path.join(objects_path, commit_id[:2], commit_id[2:])
    with open(commit_path, 'rb') as commit_file:
        commit = zlib.decompress(commit_file.read())
        header, _, body = commit.partition(b'\x00')
        body = body.decode()
        _, size = header.split()
        print(f'Commit {commit_id} with size {int(size)}\n')
        print(body)
        tree_id = body.split('tree ')[1].split()[0]
        print_commit_tree(tree_id)
        if len(body.split('parent ')) > 1:
            parent_commit_id = body.split('parent ')[1].split()[0]
            print_commit(parent_commit_id)
        

def is_tree(obj_id):
    with open(os.path.join(objects_path, obj_id[:2], obj_id[2:]), 'rb') as obj_file:
        obj = zlib.decompress(obj_file.read())
        header, _, _ = obj.partition(b'\x00')
        obj_type, _ = header.split()
        return obj_type == b'tree'


def print_commit_tree(tree_id, indent = 1):
    tree_path = os.path.join(objects_path, tree_id[:2], tree_id[2:])
    with open(tree_path, 'rb') as tree_file:
        tree = zlib.decompress(tree_file.read())
        header, _, body = tree.partition(b'\x00')
        _, size = header.split()
        while body:
            treehdr, _, treetail = body.partition(b'\x00')
            gitid, body = treetail[:20], treetail[20:]
            treehdr = treehdr.decode()
            print(f'{"|" + "-" * indent + ">"}{treehdr}, {gitid.hex()}')
            if is_tree(gitid.hex()):
                print_commit_tree(gitid.hex(), indent + 1)


if len(sys.argv) == 1:
    print_branches()
elif len(sys.argv) == 2:
    print_commit(get_head_commit_id(sys.argv[1]))
else:
    print('Usage: python3 gitter')
