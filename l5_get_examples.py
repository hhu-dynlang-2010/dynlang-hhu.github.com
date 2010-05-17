class StaticMethod(object):
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, *args):
        return self.f

def test_static():
    class A(object):
        def static():
            return 1
        static = StaticMethod(static)

    a = A()
    assert a.static() == 1


class ReadProperty(object):
    def __init__(self, f):
        self.f = f

    def __get__(self, inst, cls):
        return self.f(inst)

def test_read_property():
    class A(object):
        def __init__(self, a):
            self.a = a
        def _compute(self):
            return self.a * 5
        c = ReadProperty(_compute)
    a = A(6)
    assert a.c == 30
    a.a = 3
    assert a.c == 15
