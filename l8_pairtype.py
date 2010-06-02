class openclass(type):
    """A type with a syntax trick: 'class __extend__(t)' actually extends
    the definition of 't' instead of creating a new subclass."""
    def __new__(cls, name, bases, dict):
        if name == '__extend__':
            for cls in bases:
                for key, value in dict.items():
                    if key == '__module__':
                        continue
                    setattr(cls, key, value)
            return None
        else:
            return type.__new__(cls, name, bases, dict)

def test_extend():
    class A(object):
        __metaclass__ = openclass
    a = A()
    assert not hasattr(a, "x")
    assert not hasattr(A, "x")
    class __extend__(A):
        x = 1
    assert a.x == A.x == 1


cache = {}

def pairtype(cls1, cls2):
    if (cls1, cls2) in cache:
        return cache[(cls1, cls2)]

    base1 = cls1.__base__
    base2 = cls2.__base__
    if cls1 is object:
        if cls2 is object:
            parents = (tuple, )
        else:
            parents = (pairtype(object, base2), )
    else:
        if cls2 is object:
            parents = (pairtype(base1, object), )
        else:
            parents = (pairtype(cls1, base2), pairtype(base1, cls2))
    result = openclass("pairtype(%s, %s)" % (cls1.__name__, cls2.__name__), parents, {})
    cache[(cls1, cls2)] = result
    return result

def pair(a, b):
    cls = pairtype(a.__class__, b.__class__)
    return cls([a, b])

def test_pairtype():
    class B(object):
        pass
    class A(B):
        pass
    P = pairtype(A, A)
    assert len(P.__bases__) == 2
    assert P.__bases__[0] is pairtype(A, B)
    
    p = pair(2, "hallo")
    assert isinstance(p, pairtype(int, str))
    assert isinstance(p, tuple)
    assert p[0] == 2
    assert p[1] == "hallo"

    class __extend__(pairtype(int, str)):
        def multiply(self):
            a, b = self
            return a * b

    assert p.multiply() == "hallohallo"

def test_pairtype_method():
    class __extend__(pairtype(int, int)):
        def add(self):
            a, b = self
            return "int: %s + %s" % (a, b)
    class __extend__(pairtype(bool, bool)):
        def add(self):
            a, b = self
            return "bool: %s + %s" % (a, b)
    assert pair(1, 5).add() == "int: 1 + 5"
    assert pair(1, True).add() == "int: 1 + True"
    assert pair(True, False).add() == "bool: True + False"
    class __extend__(pairtype(object, object)):
        def add(self):
            a, b = self
            return "object: %s + %s" % (a, b)

    assert pair(True, 1).add() == "int: True + 1"
    assert pair(True, "str").add() == "object: True + str"
