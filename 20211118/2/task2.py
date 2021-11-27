class Num:
    def __get__(self, obj, cls):
        return 0 if not hasattr(obj, '___n___') else obj.___n___

    def __set__(self, obj, val):
        if hasattr(val, 'real'):
            obj.___n___ = val
        elif hasattr(val, '__len__'):
            obj.___n___ = val.__len__()

import sys
exec(sys.stdin.read())
