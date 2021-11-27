def objcount(base_class):
    class DecoratedClass(base_class):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if hasattr(DecoratedClass, 'counter'):
                DecoratedClass.counter += 1
            else:
                DecoratedClass.counter = 1

        def __del__(self):
            DecoratedClass.counter -= 1
            if hasattr(super(), '__del__'):
                super().__del__()
    return DecoratedClass

import sys
exec(sys.stdin.read())
