class SingletonMeta(type):
    def __init__(self, name, bases, dictionary):
        self._obj = None

    def __call__(self, *args):
        if self._obj is not None:
            return self._obj
        self._obj = type.__call__(self, *args)
        return self._obj


def test_simple():
    class A(object):
        __metaclass__ = SingletonMeta
        def __init__(self):
            self.a = 5

    a1 = A()
    a2 = A()
    assert a1 is a2
    assert a1.a == 5

def test_with_init():
    class A(object):
        __metaclass__ = SingletonMeta
        def __init__(self, a):
            self.a = a

    a1 = A(1)
    a2 = A(2)
    assert a1 is a2
    assert a1.a == 1
