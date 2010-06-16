import py

from simpleparser import parse
from objmodel import W_NormalObject
from interpreter import Interpreter

def test_implicit_parent():
    ast = parse("""
k = 10
object a:
    z = k
az = a z
""")
    interpreter = Interpreter()
    # make_module creates a new empty W_NormalObject for now
    # this will change on Blatt 9
    w_module = interpreter.make_module()
    interpreter.eval(ast, w_module)
    assert w_module.getvalue("a").getvalue('__parent__') is w_module
    assert w_module.getvalue("a").getparents() == [w_module]
    assert w_module.getvalue("az").value == 10

def test_implicit_parent_method():
    ast = parse("""
k = 10
def f(x):
    if x:
        k
    else:
        1
f1 = f(1)
f0 = f(0)
""")
    interpreter = Interpreter()
    w_module = interpreter.make_module()
    interpreter.eval(ast, w_module)
    assert w_module.getvalue("f1").value == 10
    assert w_module.getvalue("f0").value == 1

def test_shadow_parent_attribute():
    ast = parse("""
k = 10
def f(x):
    if x:
        k = 41
    k
f1 = f(1)
f0 = f(0)

object a:
    k = 11

ak = a k
""")
    interpreter = Interpreter()
    w_module = interpreter.make_module()
    interpreter.eval(ast, w_module)
    assert w_module.getvalue("f1").value == 41
    assert w_module.getvalue("f0").value == 10
    assert w_module.getvalue("ak").value == 11
    assert w_module.getvalue("k").value == 10

def test_capture():
    ast = parse("""
k = 10
object a:
    j = k
k = 11
aj = a j
""")
    interpreter = Interpreter()
    w_module = interpreter.make_module()
    interpreter.eval(ast, w_module)
    assert w_module.getvalue("aj").value == 10


def test_override__parent__():
    ast = parse("""
k = 10
object a:
    x = 1
    y = 2
    z = k
object b:
    __parent__ = a
    y = 5
    z = y

ax = a x
ay = a y
az = a z
bx = b x
by = b y
bz = b z
""")
    interpreter = Interpreter()
    w_module = interpreter.make_module()
    interpreter.eval(ast, w_module)
    a = w_module.getvalue("a")
    assert a.getvalue('__parent__') is w_module
    assert w_module.getvalue("b").getvalue('__parent__') is a
    assert w_module.getvalue("b").getparents() == [a]
    assert w_module.getvalue("ax").value == 1
    assert w_module.getvalue("ay").value == 2
    assert w_module.getvalue("az").value == 10
    assert w_module.getvalue("bx").value == 1
    assert w_module.getvalue("by").value == 5
    assert w_module.getvalue("bz").value == 5

def test_parent_syntax():
    ast = parse("""
object a:
    x = 11
object b(parent=a):
    x = 22
af = a x
bf = b x
""")
    interpreter = Interpreter()
    w_module = interpreter.make_module()
    interpreter.eval(ast, w_module)
    a = w_module.getvalue("a")
    b = w_module.getvalue("b")
    assert a.getvalue('__parent__') is w_module
    assert b.getvalue('__parent__') is w_module
    assert b.getvalue('parent') is a
    assert a.getparents() == [w_module]
    assert b.getparents() == [a, w_module]
    assert w_module.getvalue("af").value == 11
    assert w_module.getvalue("bf").value == 22

def test_parent_syntax_multiple():
    ast = parse("""
a = 1
b = 2
c = 3
d = 4
object x:
    b = 5
    c = 6
    d = 7
object y:
    c = 8
    d = 9
object z(p1=y, p2=x):
    d = 10
za = z a
zb = z b
zc = z c
zd = z d
""")
    interpreter = Interpreter()
    w_module = interpreter.make_module()
    interpreter.eval(ast, w_module)
    x = w_module.getvalue("x")
    y = w_module.getvalue("y")
    z = w_module.getvalue("z")
    assert x.getvalue('__parent__') is w_module
    assert y.getvalue('__parent__') is w_module
    assert z.getvalue('__parent__') is w_module
    assert z.getvalue('p1') is y
    assert z.getvalue('p2') is x
    assert x.getparents() == [w_module]
    assert y.getparents() == [w_module]
    assert z.getparents() == [y, x, w_module]
    assert w_module.getvalue("za").value == 1
    assert w_module.getvalue("zb").value == 5
    assert w_module.getvalue("zc").value == 8
    assert w_module.getvalue("zd").value == 10

def test_wrong_hierarchy_error():
    ast = parse("""
object base:
    x = 1
object sub(p1=base):
    x = 2
def mayhem:
    object bad(p1=base, p2=sub):
        x = 3
    bad x
result = mayhem
""")
    interpreter = Interpreter()
    w_module = interpreter.make_module()
    py.test.raises(TypeError, interpreter.eval, ast, w_module)

def test_duplicate_base_error():
    ast = parse("""
object base:
    x = 1
object sub(p1=base, p2=base):
    x = 2
y = sub x
""")
    interpreter = Interpreter()
    w_module = interpreter.make_module()
    py.test.raises(TypeError, interpreter.eval, ast, w_module)

