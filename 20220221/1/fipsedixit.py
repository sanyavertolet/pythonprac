import ipsedixit
import os
import sys

defaults = ['caesar', 'tacitus']

if sys.argv[2] in defaults or os.path.isfile(sys.argv[2]):
    if sys.argv[2] in defaults:
        text = sys.argv[2]
    elif os.path.isfile(sys.argv[2]):
        with open(sys.argv[2], encoding='utf-8') as input_file:
            text = input_file.read()
    generator = ipsedixit.Generator(text)
    sys.argv.pop(2)
else:
    generator = ipsedixit.Generator()
args = ipsedixit.parse_args()
print('\n\n'.join(generator.paragraphs(args.num, args.min, args.max)))

