>>> # _________________________________________________________
>>> # override getitem
>>>
>>> class A(object):
...     def __getitem__(self, i):
...         return i + 1
... 
>>> a = A()
>>> a[1]
2
>>> a[9]
10
>>> class B(object):
...      def __setitem__(self, name, val):
...          print name, val
... 
>>> b = B()
>>> b["abc"] = 12
abc 12
>>> b[None] = 12
None 12
>>> dict.__getitem__
<method '__getitem__' of 'dict' objects>
>>> d = {}
>>> d["a"] = 12
>>> d
{'a': 12}
>>> d.__setitem__("b", 15)
>>>
>>>
>>> # _________________________________________________________
>>> # override comparison
>>>
>>> class A(object):
...     def __init__(self, a):
...         self.a = a
...     def __cmp__(self, other):
...         if self.a == other.a:
...              return 0
...         if self.a > other.a:
...              return -1
...         return 1
... 
>>> a1 = A(5)
>>> a2 = A(7)
>>> a1 < a2
False
>>> a1 < a2
False
>>> A(5) < A(7)
False
>>> A(5) < A(7)
False
>>> A(5) < A(12)
False
>>> A(5) < A(5)
False
>>> A(5) < A(3)
True
>>> A(5) == A(5)
True
>>> A(5) <= A(5)
True
>>> 
>>> 
>>> 
>>> # _________________________________________________________
>>> # overriding multiplication, reverse multiplication, NotImplemented
>>> 
>>> class A(object):
...    pass
... 
>>> x = 5
>>> x.__mul__(A())
NotImplemented
>>> x * A()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for *: 'int' and 'A'
>>> x.__mul__(4.5)
NotImplemented
>>> f = 4.5
>>> f.__rmul__(5)
22.5
>>> class A(object):
...     def __mul__(self, other):
...         print "__mul__ called", self, other
...         return NotImplemented
... 
>>> class B(object):
...     def __rmul__(self, other):
...         print "__rmul__ called", self, other
...         return 7
... 
>>> a = A()
>>> b = B()
>>> a * b
__mul__ called <__main__.A object at 0x86af22c> <__main__.B object at 0xb74c0a6c>
__rmul__ called <__main__.B object at 0xb74c0a6c> <__main__.A object at 0x86af22c>
7
>>> b * a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for *: 'B' and 'A'
>>> def __mul__(self, other):
...       return NotImplemented
... 
>>> B.__mul__ = __mul__
>>> b * a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for *: 'B' and 'A'
>>> 
>>> 
>>> # _________________________________________________________
>>> # overriding call
>>> 
>>> class Callable(object):
...     def __call__(self, *args):
...         return len(args)
... 
>>> c = Callable()
>>> c()
0
>>> c(1)
1
>>> c(1, 3)
2
>>> c(1, 3, 4)
3
>>> def f(x):
...     return x + 5
... 
>>> f(10)
15
>>> c(1, 3)
2
>>> f.__call__
<method-wrapper '__call__' of function object at 0xb74bb80c>
>>> f.__call__(7)
12
>>> f.__call__.__call__(7)
12
>>> f.__call__.__call__.__call__(7)
12
>>> f
<function f at 0xb74bb80c>
>>> f.__class__
<type 'function'>
>>> f.__class__.__call__
<slot wrapper '__call__' of 'function' objects>
>>> f.__class__.__base__
<type 'object'>
>>> f.__class__.__base__.__call__
<method-wrapper '__call__' of type object at 0x82358a0>
>>> f()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes exactly 1 argument (0 given)
>>> f(8)
13
>>> o = object()
>>> o()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'object' object is not callable
>>> o.__call__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'object' object has no attribute '__call__'
>>> object.__call__
<method-wrapper '__call__' of type object at 0x82358a0>
>>> o.__call__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'object' object has no attribute '__call__'
>>>
>>>
>>> # _________________________________________________________
>>> # __get__ special method
>>>
>>> def f(a, b):
...     return a * b
... 
>>> f.__get__
<method-wrapper '__get__' of function object at 0xb74bb79c>
>>> m = f.__get__(6)
>>> m
<bound method ?.f of 6>
>>> m(8)
48
