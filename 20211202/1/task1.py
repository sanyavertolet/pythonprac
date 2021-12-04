import types
from functools import wraps

class dump(type):
    def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)
    
    def __new__(cls, name, parents, ns):
        return super().__new__(cls, name, parents, ns)

    def __init__(self, name, parents, namespace):
        for fname in namespace:
            fun = namespace[fname]
            if isinstance(fun, types.FunctionType):
                @wraps(fun)
                def new_fun(*args, fname=fname, fun=fun, **kwargs):
                    print(f'{fname}: {args[1:]}, {kwargs}')
                    return fun(*args, **kwargs)
                setattr(self, fname, new_fun)
        return super().__init__(name, parents, namespace)

import sys
exec(sys.stdin.read())

