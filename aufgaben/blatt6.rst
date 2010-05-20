
=======================================
Dynamic Languages - Übungen Blatt 6
=======================================

:Abgabedatum: ``11. December 2008``
:Subversion URL: svn://wyvern.cs.uni-duesseldorf.de/dynlang08


Aufgabe 1 - Sudoku
------------------

Write a Sudoku solver.  Use a generator that takes as argument a partial
board, chooses an unfilled position, and enumerates all valid boards
that have this position filled.

Remember to write tests first.


Aufgabe 2 - Prototypes (2)
--------------------------

* Modify the solution to Blatt 4, Aufgabe 2 (Prototypes) so that every
  prototype object has several parents instead of one.  This is done by
  replacing "parent" by "parents", which is now a list of parent objects
  (or ``[]`` if none, instead of ``None``).

  See the exercice for a first test.  Adapt all the other tests from
  ``blatt4.py``.

* Modify the algorithm looking for attribute by parents to implement
  proper support for multiple inheritance.  The goal is to make it pass
  ``test_mro()``, where ``d.x`` should not return 5 (as is done by a
  simple left-to-right search) but 4.  One such algorithm is as follows.
  First list the lookup order taken by the simple-minded left-to-right
  algorithm; in this case, it should be ``d, b, a, c, a``.  Then remove
  all duplicate objects, keeping only the last one, getting ``d, b, c,
  a``.  Then do the lookup in that order.
