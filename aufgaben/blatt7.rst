=======================================
Dynamic Languages - Übungen Blatt 7
=======================================

:Abgabedatum: ``18. December 2008``
:Subversion URL: svn://wyvern.cs.uni-duesseldorf.de/dynlang08


This are the first in a series of exercises to build an interpreter for a small
prototype-based language. The parser for the language exists already. To get an
impression of how the language looks like, look at the docstrings in the AST
node classes and at the tests. All the neccessary files can be found in the
``aufgaben/simple`` directory. Please don't change any of the existing files,
so that future additions from our side are possible.

You can ignore parents for this week.


Aufgabe 1 - Basic Object Model
-------------------------------

Start implementing the prototype-based object model of the language. There are
three types of objects: integers, "normal" objects and methods. These three
types of objects should correspond to three classes in your source code that
implement them. Integers just have an integer value. Normal objects have a set
of attributes. Methods are like normal objects but in addition they also have a
reference to an AST node that the parser produces which describes how the
method behaves.

As opposed to the earlier exercises, these classes should not be usable from
Python (so there is no need to override e.g. ``__getattr__``). Instead they
should have an interface that the interpreter can use. There are some tests
about this in ``aufgaben/simple/test_objmodel.py``. Write more.


Aufgabe 2 - Simple Interpreter
-------------------------------

Write a simple interpreter. ``:-)``

It is fine if we get an exception in unsupported cases.  The test files
should pass, though.  As usual, write more tests.
