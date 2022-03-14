#!/usr/bin/python3.10
import ast
import re
import sys
import textdistance

def get_usrc(fname):
    with open(fname) as f:
        return ast.unparse(ast.parse(f.read()))
    
def get_tree(node):
    ast_tree = ast.dump(ast.NodeTransformer().generic_visit(node), annotate_fields=False)
    return ast_tree

def resub(src):
    #src = re.sub()
    src = re.sub('\s*', '', src)
    src = re.sub('\'[^\']*\'', '', src)
    src = re.sub('\'\'\'[^\'\'\']*\'\'\'', '', src)
    src = re.sub('\"[^\"]*\"', '', src)
    src = re.sub('\"\"\"[^\"\"\"]*\"\"\"', '', src)
    src = re.sub('[A-Z]([^(\(|\[)])*\([^A-Z\[\()\],]*', '`(', src)
    src = re.sub('[A-Z]([^(\(|\[)])*\[[^A-Z\[\()\],]*', '`[', src)
    return src

if len(sys.argv) == 3:
    src1 = get_usrc(sys.argv[1])
    src2 = get_usrc(sys.argv[2])
    
    src1 = get_tree(ast.parse(src1))
    src2 = get_tree(ast.parse(src2))
    
    src1 = resub(src1)
    src2 = resub(src2)

    ratio = textdistance.damerau_levenshtein.normalized_distance(src1, src2)
    print(ratio)
    if ratio < 0.1:
        print('Stolen!!')
    else:
        print('Not stolen.')
else:
    print('Usage: antip.py file1.py file2.py')

