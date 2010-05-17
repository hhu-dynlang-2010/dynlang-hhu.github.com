# ___________________________________________________________________
# Aufgabe 1

def test_logging_proxy_simple():
    class A(object):
        def __init__(self, a):
            self.a = a

        def f(self, x):
            result = self.a
            self.a = x
            return result

    a = A(1)
    p = LoggingProxy(a)
    assert p.a == 1
    attr = p.f(10)
    assert attr == 1
    assert p.a == 10
    assert get_proxy_log(p) == ["a", "f", "a"]

def test_logging_proxy_special():
    p = LoggingProxy(41.0)
    assert p + 2 == 43.0
    assert p - 2 == 39.0
    assert p == 41.0
    assert p
    assert p * 2 == 82.0
    assert p // 2 == 20.0
    assert p > 1.0
    assert get_proxy_log(p) == ["__add__", "__sub__", "__eq__", "__nonzero__",
                                "__mul__", "__floordiv__", "__gt__"]


# ___________________________________________________________________
# prototypes - Aufgabe 2

import py

def test_simple():
    x1 = ProtoObject({"a": 1})
    assert x1.a == 1
    x1.a = 2
    assert x1.a == 2
    assert x1.parent is default_parent
    assert default_parent.parent is None

    y = ProtoObject({"b": 1, "parent": x1})
    assert y.b == 1
    assert y.a == 2
    y.a = 3
    assert y.a == 3
    assert x1.a == 3

    x2 = ProtoObject({"c": 41})
    y.parent = x2
    assert y.b == 1
    assert y.c == 41
    py.test.raises(AttributeError, "y.a")

def test_write():
    x1 = ProtoObject({"a": 1})
    x2 = ProtoObject({"b": 1, "parent": x1})
    assert x2.a == 1
    x2.a = 2
    assert x1.a == 2
    assert x2.a == 2
    x2.b = 2
    assert x2.b == 2
    py.test.raises(AttributeError, "x1.b")
    x2.c = 1
    assert x2.c == 1
    py.test.raises(AttributeError, "x1.c")



def test_syntax():
    class x1:
        __metaclass__ = ProtoMeta
        a = 1

    assert isinstance(x1, ProtoObject)
    assert x1.a == 1
    x1.a = 2
    assert x1.a == 2

    class y:
        __metaclass__ = ProtoMeta
        b = 1
        parent = x1

    assert isinstance(y, ProtoObject)
    assert y.b == 1
    assert y.a == 2
    y.a = 3
    assert y.a == 3
    assert x1.a == 3

    class x2:
        __metaclass__ = ProtoMeta
        c = 41

    y.parent = x2
    assert y.b == 1
    assert y.c == 41
    py.test.raises(AttributeError, "y.a")


def test_method():
    class x1:
        __metaclass__ = ProtoMeta
        a = 1
        def f(self, x):
            return self.a + x
    assert x1.f(10) == 11
    x1.a = 34
    assert x1.f(10) == 44

    class y:
        __metaclass__ = ProtoMeta
        a = 2
        parent = x1

    assert y.f(10) == 12
    f = y.f
    assert f(11) == 13
    y.a = 34
    assert y.f(10) == 44

def test_clone():
    empty = default_parent.clone()
    assert empty is not default_parent
    assert empty.parent is None

    class x1:
        __metaclass__ = ProtoMeta
        a = 1
    x2 = x1.clone()
    assert x2.a == 1
    x2.a = 34
    assert x2.a == 34
    assert x1.a == 1

def test_override_clone():

    class x1:
        __metaclass__ = ProtoMeta
        distance = 1
        a = 23
        def clone(self):
            class cloned:
                __metaclass__ = ProtoMeta
                distance = self.distance + 1
                a = self.a
            return cloned

    x2 = x1.clone()
    assert x1 is not x2
    assert x2.distance == 2
    assert x2.a == 23
    x2.a = 24
    assert x2.a == 24
    assert x1.a == 23

    # default clone is used here
    x3 = x2.clone()
    assert x3.distance == 2
    assert x3.a == 24
