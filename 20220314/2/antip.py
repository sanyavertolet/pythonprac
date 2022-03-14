#!/usr/bin/python3.10
import ast
import re
import sys
import textdistance

def get_utree(fname):
    with open(fname) as f:
        src = ast.dump(ast.NodeTransformer().generic_visit(ast.parse(ast.unparse(ast.parse(f.read())))), annotate_fields=False)
    src = re.sub('\s*', '', src)
    src = re.sub('\'[^\']*\'', '', src)
    src = re.sub('\'\'\'[^\'\'\']*\'\'\'', '', src)
    src = re.sub('\"[^\"]*\"', '', src)
    src = re.sub('\"\"\"[^\"\"\"]*\"\"\"', '', src)
    src = re.sub('[a-z]([^(\(|\[)])*\([^A-Z\[\()\],]*', '(', src)
    return re.sub('[a-z]([^(\(|\[)])*\[[^A-Z\[\()\],]*', '[', src)

if len(sys.argv) == 3:
    src = [get_utree(sys.argv[i]) for i in range(1, len(sys.argv))]
    print('Stolen!!' if textdistance.damerau_levenshtein.normalized_distance(*src) < 0.1 else 'Not stolen.')
else:
    print('Usage: antip.py file1.py file2.py')

