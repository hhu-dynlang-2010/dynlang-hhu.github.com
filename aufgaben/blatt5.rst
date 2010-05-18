=======================================
Dynamic Languages - Übungen Blatt 5
=======================================

:Abgabedatum: ``25. Main 2010``


Aufgabe 1
---------

(2 Punkte)

Complete the exercice given by ``class TreeNode`` to add the methods
``enumerate()``, ``enumerate_first()`` and ``enumerate_last()`` to match the
test.  Use generators!


Aufgabe 2
---------

(2 Punkte)

Write some tests for a function ``sum(iterable)`` that returns an
iterator, where the nth element of the result is the sum of all elements
0 to n of the argument ``iterable``.  In other words, ``sum(iterable)``
returns an iterator yielding ``iterable[0]``, then ``iterable[0] +
iterable[1]``, then ``iterable[0] + iterable[1] + iterable[2]``, etc.

Remember that at least one test should be about taking an infinite
iterable.  One such iterable could be ``itertools.count()``; look it
up in the on-line help with ``help(itertools.count)``.

Then write the function itself.


Aufgabe 3
---------

(6 Punkte)

Implement a game starting from the file ``pygame_game.py``.  In this game,
we should have 10 "attacker" rectangles moving semi-randomly to the
player.  The player should be movable by clicking on the window where we
want it to go; it should move there at some speed, and loose when it
touches one of the attackers. Feel free to extend the game in any way.

All moving entites ("sprites") should be implemented by writing
a generator in their ``run()`` method.
