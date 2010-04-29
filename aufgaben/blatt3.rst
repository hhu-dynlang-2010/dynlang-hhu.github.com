=======================================
Dynamic Languages - Übungen Blatt 3
=======================================

:Abgabedatum: 20. November 2008
:Subversion URL: svn://wyvern.cs.uni-duesseldorf.de/dynlang08


Aufgabe 1 - Proxies
-------------------

Implement a logging proxy object. Its constructor takes an arbitrary
object. The proxy is supposed to keep a list of all attribute that were
accessed on the object, including special methods, in order of access.
The log can be accessed using a global function ``get_proxy_log``. The
test functions are given in ``aufgaben/blatt3.py``.

In addition, write another test function with a proxy around a
dictionary, testing at least the special methods ``__getitem__`` and
``__setitem__``.

Ideally, your source code should not define all ``__xxx__`` methods by
copy-pasting them in the source of the class, but by putting these
methods inside the class programmatically (with a loop).


Aufgabe 2 - Game of Life
------------------------

Implement a Game of Life simulation:
http://de.wikipedia.org/wiki/Conways_Spiel_des_Lebens

The board should be infinite.  Use a set of coordinates ``(n, m)``
representing the position of all live cells, and write a function
that computes a new set representing the next generation.

For *sets*, you can use the built-in type ``set`` (see
http://docs.python.org/library/stdtypes.html#set-types-set-frozenset).

To see the results, also write a function that turns such a set into a
multiline string, with spaces or 'X' signs.  See the test for details.


Aufgabe 3 - Lua tables
----------------------

The Lua programming language has a single data structure called *table*
instead of Python's *list* and *dict*.  A table is a dictionary-like
structure that can also behave like a list when the keys are integers.

The purpose of this exercice is to design, test and implement a simple
``Table`` class in Python.  It should have a dictionary-like interface,
supporting at least expressions like:

* ``table[key] = value``

* ``value = table[key]``

* ``key in table`` (test for existence of a key; this calls the
  ``__contains__`` special method on the table)

It should also support list-like expressions like:

* ``len(table)``, which should return the smallest integer ``n`` such
  that ``n not in table``.  For example, if the table contains the keys
  0, 1 and 2, then its length should be 3.  If the table also contains
  other keys like 42 and "hello world", then they are ignored the length
  is 3 anyway.  If the table doesn't even contain the key 0, its length
  is 0.

* ``table.append(x)``, equivalent to ``table[len(table)] = x``.

* ``del table[index]`` and ``table.insert(index, x)`` should work like
  in lists: they should remove or insert an element in the middle of
  the list, shifting the end of the list.  For example, if the table
  contains ``{0: 'x', 1: 'y'}``, then after ``del table[0]`` it
  should contain ``{0: 'y'}``.

* ``table1 + table2`` should work like list concatenation if the tables
  just contain consecutive 0-based numbers as keys.  For the cases of
  tables that also contain more keys, design a "sensible" way to put
  them in the result.

Write tests *first!*
