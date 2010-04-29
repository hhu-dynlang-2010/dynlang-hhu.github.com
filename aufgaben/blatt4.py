SQUARE = set([(0,0), (0,1),
              (1,0), (1,1)])

def test_from_life_string():
    assert from_lifestring("") == set()
    assert from_lifestring("X") == set([(0,0)])
    assert from_lifestring("X X") == set([(0, 0), (0, 2)])

    assert from_lifestring("XX\nXX") == SQUARE
    assert from_lifestring("XX\nX ") == set([(0,0), (0,1), (1,0)])



# ___________________________________________________________________
# prototypes

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
    
    x3 = x2.clone()
    assert x3.distance == 3
    assert x3.a == 23
