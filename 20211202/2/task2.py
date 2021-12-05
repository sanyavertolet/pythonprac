class check(type):
    def __init__(self, name, parents, ns):
        def check_annotations(self):
            return all([isinstance(getattr(self, varname, None), vartype) for varname, vartype in self.__annotations__.items()])
        self.check_annotations = check_annotations
        return super().__init__(name, parents, ns)

import sys
exec(sys.stdin.read())
