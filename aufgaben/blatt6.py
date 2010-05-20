import py

def test_simple():
    x1 = ProtoObject({"a": 1})
    assert x1.a == 1
    x1.a = 2
    assert x1.a == 2
    assert x1.parents == [default_parent]
    assert default_parent.parents == []

    y = ProtoObject({"b": 1, "parents": [x1]})
    assert y.b == 1
    assert y.a == 2
    y.a = 3
    assert y.a == 3
    assert x1.a == 3

    x2 = ProtoObject({"c": 41})
    y.parents = [x2]
    assert y.b == 1
    assert y.c == 41
    py.test.raises(AttributeError, "y.a")

    y.parents = [x1, x2]
    assert y.a == 3
    assert y.b == 1
    assert y.c == 41

# ____________________________________________________________

__metaclass__ = ProtoMeta

def test_mro():
    class a:
        x = 5
        z = 765
    class b:
        parents = [a]
        y = 60
        z = 764
    class c:
        parents = [a]
        x = 4
        y = 61
        z = 763
    class d:
        parents = [b, c]

    assert d.x == 4      # and not 5!
    assert d.y == 60
    assert d.z == 764
