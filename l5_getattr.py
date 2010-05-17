import py
import types

def make_method(func, self):
    def method(*args):
        return func(self, *args)
    return method

BuiltinMethod = object.__setattr__.__class__

def mygetattr_in_class(obj, attrname):
    cls = obj.__class__
    for checkcls in cls.mro():
        if attrname in checkcls.__dict__:
            attr = checkcls.__dict__[attrname]
            if not isinstance(attr, (types.FunctionType, BuiltinMethod)):
                return attr
            return attr.__get__(obj)
    raise AttributeError("attribute " + attrname + " not found")


def mygetattr(obj, attrname):
    if attrname in obj.__dict__:
        return obj.__dict__[attrname]
    try:
        return mygetattr_in_class(obj, attrname)
    except AttributeError:
        return mygetattr_in_class(obj, "__getattr__")(attrname)

def test_mygetattr():
    class A(object):
        y = 15
        def f(self, x):
            old = self.x
            self.x = x
            return old
    a = A()
    a.x = 7
    assert mygetattr(a, "x") == 7
    assert mygetattr(a, "y") == 15
    py.test.raises(AttributeError, "mygetattr(a, 'blablabla')")
    m = mygetattr(a, "f")
    v = m(5)
    assert v == 7

    assert mygetattr(a, "x") == 5

def test_mygetattr___getattr__():
    class B(object):
        def __getattr__(self, attrname):
            return attrname

    b = B()
    assert mygetattr(b, "hello") == "hello"
    b.hello = 15
    assert mygetattr(b, "hello") == 15

def test_mygetattr___getattr__2():
    class B(object):
        def __getattr__(self, attrname):
            if attrname == "foo":
                raise AttributeError
            return 17

    b = B()
    assert mygetattr(b, "hello") == 17
    b.hello = 15
    assert mygetattr(b, "hello") == 15
    py.test.raises(AttributeError, "mygetattr(b, 'foo')")
    py.test.raises(AttributeError, "b.foo")


def mysetattr(obj, attrname, value):
    try:
        mygetattr_in_class(obj, "__setattr__")(attrname, value)
    except AttributeError:
        obj.__dict__[attrname] = value

def test_mysetattr():
    class A(object):
        x = 1

    a = A()
    mysetattr(a, "y", 5)
    assert a.y == 5

    assert a.x == 1
    mysetattr(a, "x", 6)
    assert a.x == 6
    assert A.x == 1

def test_mysetattr__setattr__():
    class A(object):
        def __setattr__(self, attrname, value):
            value += 1
            self.__dict__[attrname] = value
    a = A()
    a.x = 15
    assert a.x == 16

    mysetattr(a, "x", 27)
    assert a.x == 28
