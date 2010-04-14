$ python
Python 2.6.4 (r264:75706, Dec  7 2009, 18:45:15)
[GCC 4.4.1] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> # _______________________________________________________
>>> # interactivity
>>> a = 1
>>> a
1
>>> a + 2
3
>>> s = "string"
>>> s * 5
'stringstringstringstringstring'
>>>


$ swipl
Welcome to SWI-Prolog (Multi-threaded, 32 bits, Version 5.8.3)
Copyright (c) 1990-2009 University of Amsterdam.
SWI-Prolog comes with ABSOLUTELY NO WARRANTY. This is free software,
and you are welcome to redistribute it under certain conditions.
Please visit http://www.swi-prolog.org for details.

For help, use ?- help(Topic). or ?- apropos(Word).

?- f(X) = f(a).
X = a.

?-
% halt


$ python
Python 2.6.4 (r264:75706, Dec  7 2009, 18:45:15)
[GCC 4.4.1] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> # _______________________________________________________
>>> # dynamic typing
>>> a = 1
>>> type(a)
<type 'int'>
>>> l = [1, 2, 3]
>>> l = [1, 2, "str"
... ]
>>> l
[1, 2, 'str']
>>> # _______________________________________________________
>>> # garbage collection
>>> f = file("abc.txt", "w")
>>> f.write("hallo\n")
>>> f = None
>>>
$ cat abc.txt
hallo

$ python
Python 2.6.4 (r264:75706, Dec  7 2009, 18:45:15)
[GCC 4.4.1] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> # _______________________________________________________
>>> # late binding
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> def f(x):
...      return g(x)
...
>>> g
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'g' is not defined
>>> f
<function f at 0xb750ffb4>
>>> f(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in f
NameError: global name 'g' is not defined
>>> def g(x):
...     return x + 1
...
>>> f(10)
11
>>> # _______________________________________________________
>>> # everything is an object
>>> f
<function f at 0xb750ffb4>
>>> l = [f, g]
>>> l[0](1)
2
>>> type(f)
<type 'function'>
>>> f.func_code
<code object f at 0xb7555578, file "<stdin>", line 1>
>>> f.func_name
'f'
>>> l[0].func_name
'f'
>>> int
<type 'int'>
>>> str
<type 'str'>
>>> l2 = [int, str]
>>> l2[0]("123")
123
>>> f.func_name = "hello"
>>> f
<function hello at 0xb750ffb4>
>>>
>>>
>>>
>>>
>>>
>>>
>>> # _______________________________________________________
>>> # integers, longs, floats
>>> a = 1
>>> a * 5
5
>>> 2 * 5
10
>>> 2 ** 1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376L
>>> 12.234
12.234
>>> 12.234 + 123.521
135.755
>>> 1.0 / 3
0.33333333333333331
>>>

>>> # _______________________________________________________
>>> # strings
>>> s = "abc"
>>> t = 'abc'
>>> s == t
True
>>> s = "'hello'"
>>> s
"'hello'"
>>> s + t
"'hello'abc"
>>> s * 10
"'hello''hello''hello''hello''hello''hello''hello''hello''hello''hello'"
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> "hello world".capitalize()
'Hello world'
>>> "hello world".title()
'Hello World'
>>> s = "hello world"
>>> s.find("w")
6
>>> s[1]
'e'
>>> type(s[1])
<type 'str'>
>>> type(s)
<type 'str'>
>>> len(s[1])
1
>>> s.find("abc")
-1
>>> s.split()
['hello', 'world']

>>> # _______________________________________________________
>>> # lists
>>> l = [1, 2, 3, 4, 5, 6]
>>> l
[1, 2, 3, 4, 5, 6]
>>> len(l)
6
>>> l[0]
1
>>> l[2]
3
>>> l[0:3]
[1, 2, 3]
>>> l[0:len(l)]
[1, 2, 3, 4, 5, 6]
>>> l[0:5] == l[:5]
True
>>> l[2:len(l)] == l[2:]
True
>>> l[:]
[1, 2, 3, 4, 5, 6]
>>> l[:]
[1, 2, 3, 4, 5, 6]
>>> l2 = l[:]
>>> l2 is l
False
>>> l2 == l
True
>>> l[0] = 6
>>> l
[6, 2, 3, 4, 5, 6]
>>> l2
[1, 2, 3, 4, 5, 6]
>>> l[0:2] = [1, 4]
>>> l
[1, 4, 3, 4, 5, 6]
>>> l[0:2] = [1, 4, 5, 6, 7, 8, 9]
>>> l
[1, 4, 5, 6, 7, 8, 9, 3, 4, 5, 6]
>>> l[1:7]
[4, 5, 6, 7, 8, 9]
>>> l[1:7:2]
[4, 6, 8]
>>> l[1:7:]
[4, 5, 6, 7, 8, 9]
>>> l[1:7:-1]
[]
>>> l[7:1:-1]
[3, 9, 8, 7, 6, 5]
>>> l[::-1]
[6, 5, 4, 3, 9, 8, 7, 6, 5, 4, 1]
>>> l
[1, 4, 5, 6, 7, 8, 9, 3, 4, 5, 6]
>>> l.append(1)
>>> l
[1, 4, 5, 6, 7, 8, 9, 3, 4, 5, 6, 1]
>>> l.append(5)
>>> l
[1, 4, 5, 6, 7, 8, 9, 3, 4, 5, 6, 1, 5]
>>> l.extend([41, 42, 43, 44])
>>> l
[1, 4, 5, 6, 7, 8, 9, 3, 4, 5, 6, 1, 5, 41, 42, 43, 44]
>>> l.pop()
44
>>> l.pop()
43
>>> l.pop()
42
>>> l.pop()
41
>>> l
[1, 4, 5, 6, 7, 8, 9, 3, 4, 5, 6, 1, 5]
>>> l.sort()
>>> l
[1, 1, 3, 4, 4, 5, 5, 5, 6, 6, 7, 8, 9]
>>> "abc" < "def"
True
>>> "abc" < "def"
True
>>> ["a", "c", "z", a"]
  File "<stdin>", line 1
    ["a", "c", "z", a"]
                      ^
SyntaxError: EOL while scanning string literal
>>> l = ["a", "c", "z", "a"]
>>> l.sort()
>>> l
['a', 'a', 'c', 'z']
>>> dir(l)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> l.count("a")
2
>>> l.index("z")
3
>>> l.reverse
<built-in method reverse of list object at 0x856784c>
>>> l.reverse()
>>> l
['z', 'c', 'a', 'a']
>>> l.reverse
<built-in method reverse of list object at 0x856784c>
>>> l.__len__()
4
>>> len(s)
11
>>> len(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'int' has no len()
>>> a = 1
>>> a.__len__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute '__len__'

>>> # _______________________________________________________
>>> # dicts
>>> d = {"david": 42, "carl friedrich": 43}
>>> d
{'carl friedrich': 43, 'david': 42}
>>> d["david"]
42
>>> len(d)
2
>>> d.keys()
['carl friedrich', 'david']
>>> d.values()
[43, 42]
>>> len
<built-in function len>

>>> # _______________________________________________________
>>> # if statement
>>> x = 1
>>> if x > 0:
...     print "hello"
...
hello
>>> if x < 0:
...     bla(x)
... else:
...     print "bye"
...
bye
>>> x = 0
>>> while x < 100:
...     print x
...     x += 1
...
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
>>> # _______________________________________________________
>>> # while loop
>>> x = 0
>>> while x < 10:
...     if x == 8:
...         break
...     x += 1
...     print x
...
1
2
3
4
5
6
7
8
>>> # _______________________________________________________
>>> # for loop
>>> l = [1, 5, 8, 12]
>>> for element in l:
...     print l
...
[1, 5, 8, 12]
[1, 5, 8, 12]
[1, 5, 8, 12]
[1, 5, 8, 12]
>>> for element in l:
...     print element
...
1
5
8
12
>>> for element in "hello":
...     print element
...
h
e
l
l
o
>>> for element in "hello":
...
  File "<stdin>", line 2

    ^
IndentationError: expected an indented block
>>> d
{'carl friedrich': 43, 'david': 42}
>>> for e in d:
...     print e
...
carl friedrich
david
>>> for key, value in d.items():
...     print key, value
...
carl friedrich 43
david 42
>>> d.items()
[('carl friedrich', 43), ('david', 42)]
>>> d.items()
[('carl friedrich', 43), ('david', 42)]

>>> # _______________________________________________________
>>> # function definition
>>> def function(a, b, c):
...     return a + b * c
...
>>> function(1, 2, 5)
11
>>> function("hello ", "world", 5)
'hello worldworldworldworldworld'
>>> function(1.1, 2.1, 5.1)
11.809999999999999
>>>
>>> range(6)
[0, 1, 2, 3, 4, 5]
>>> range(2, 6)
[2, 3, 4, 5]
>>> range(6, -1, -1)
[6, 5, 4, 3, 2, 1, 0]
>>> for i in range(10):
...     print i
...
0
1
2
3
4
5
6
7
8
9
>>>
