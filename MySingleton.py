from typing import Any


class SingletonType(type):
    _instances={}
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self not in self._instances:
            obj=super().__call__(*args, **kwds)
            self._instances[self]=obj
            return obj
        return self._instances[self]

class Logger(metaclass=SingletonType):
    pass

class Mogger(metaclass=SingletonType):
    pass

l1=Logger() # Logger.__call__(fish, rice,dodo=moo)
l2=Logger() # Logger.__call__(kimbo)
m1=Mogger() # Mogger.__call__(mimbo)
m2=Mogger() # Mogger.__call__(mimbo)
assert l1 is l2
assert m1 is m2