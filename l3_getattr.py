import py
import types

# ____________________________________________________________ 
# simulate a bound method object using a nested function

def make_method(func, inst):
    def method(*args):
        return func(inst, *args)
    return method


# ____________________________________________________________
# reimplementation of getattr using pure Python


BuiltinMethod = list.append.__class__

def mygetattr(inst, attrname):
    # check whether the attribute is found in the objects dictionary
    if hasattr(inst, "__dict__") and attrname in inst.__dict__:
        return inst.__dict__[attrname]
    cls = inst.__class__
    # walk up the method-resolution-order to find the attribute on the class
    for checkcls in cls.mro():
        if attrname in checkcls.__dict__:
            x = checkcls.__dict__[attrname]
            # if the attribute is a method, bind it
            if isinstance(x, types.FunctionType) or isinstance(x, BuiltinMethod):
                x = make_method(x, inst)
            return x
    # the attribute was not found in a normal way
    # look for the special method "__getattr__" and call it if found
    for checkcls in cls.mro():
        if "__getattr__" in checkcls.__dict__:
            func = checkcls.__dict__["__getattr__"]
            return func(inst, attrname)
    raise AttributeError("attribute %s not found in %s" % (attrname, inst))


def test_mygetattr():
    class C(object):
        a = 5
        def f(self):
            return 42
    c = C()
    assert mygetattr(c, "a") == 5
    c.x = 31
    assert mygetattr(c, "x") == 31
    c.a = 55
    assert mygetattr(c, "a") == 55
    meth = mygetattr(c, "f")
    assert meth() == 42

def test_mygetattr_nodict():
    l = []
    append = mygetattr(l, "append")
    append(1)
    append(2)
    append(3)
    assert l == [1, 2, 3]


def test___getattr__special_method():
    class C(object):
        def __getattr__(self, attrname):
            return len(attrname)
    c = C()
    assert mygetattr(c, "hello") == 5

# ____________________________________________________________
# reimplementation of setattr using pure Python

def mysetattr(inst, attrname, value):
    cls = inst.__class__
    for checkcls in cls.mro():
        if "__setattr__" in checkcls.__dict__:
            func = checkcls.__dict__["__setattr__"]
            func(inst, attrname, value)
            return
    inst.__dict__[attrname] = value


def test_mysetattr():
    class C(object):
        pass
    c = C()
    mysetattr(c, "a", 42)
    assert c.__dict__ == {"a": 42}

def test___setattr__special_method():
    class D(object):
        def __setattr__(self, name, value):
            self.seen.append((name, value))

    d = D()
    d.__dict__["seen"] = []
    mysetattr(d, "a", 42)
    assert d.seen == [("a", 42)]
    py.test.raises(AttributeError, "d.a")
