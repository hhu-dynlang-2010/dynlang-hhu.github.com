import py

# _________________________________________________________
# simulating the issubclass and isinstance builtin


class A(object):
    pass

class B(A):
    pass

def myissubclass(basecls, cls):
    if basecls is cls:
        return True
    if cls.__base__ is None:
        return False
    return myissubclass(basecls, cls.__base__)

def test_myissubclass():
    assert myissubclass(B, B)
    assert myissubclass(A, B)
    assert myissubclass(object, B)

    assert myissubclass(object, A)
    assert myissubclass(A, A)

    assert myissubclass(object, object)


def myisinstance(obj, cls):
    return myissubclass(cls, obj.__class__)

def test_myisinstance():
    b = B()
    assert myisinstance(b, B)
    assert myisinstance(b, A)
    assert myisinstance(b, object)

    a = A()
    assert not myisinstance(a, B)
    assert myisinstance(a, A)
    assert myisinstance(a, object)


# _________________________________________________________
# manually implementing message sending


class X(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def f(self):
        return self.x + self.y
    def setx(self, x):
        self.x = x


class Y(X):
    def g(self):
        self.x += 1

def send(obj, name, *args):
    cls = obj.__class__
    while cls is not None:
        if name in cls.__dict__:
            return cls.__dict__[name](obj, *args)
        cls = cls.__base__
    raise AttributeError("object has no attribute " + name)


def test_send():
    a = X(1, 5)
    assert send(a, "f") == 6 # equivalent to a.f()
    send(a, "setx", 6)
    assert a.x == 6

    b = Y(5, 6)
    assert send(b, "f") == 11 # equivalent to b.f()

    send(b, "g")
    assert b.x == 6

    py.test.raises(AttributeError, 'send(a, "hello")')
