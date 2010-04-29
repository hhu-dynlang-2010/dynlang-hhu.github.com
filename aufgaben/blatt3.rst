=======================================
Dynamic Languages - Übungen Blatt 3
=======================================

:Abgabedatum: ``10. Mai 2010``


Aufgabe 1 - Game of Life
------------------------

(3 Punkte)

Implement a Game of Life simulation:
http://de.wikipedia.org/wiki/Conways_Spiel_des_Lebens

The board should be infinite.  Use a set of coordinates ``(n, m)``
representing the position of all live cells, and write a function
that computes a new set representing the next generation.

For *sets*, you can use the built-in type ``set`` (see
http://docs.python.org/library/stdtypes.html#set-types-set-frozenset).

To see the results, also write a function that turns such a set into a
multiline string, with spaces or 'X' signs.  See the test for details.


Aufgabe 2 - Pygame
------------------

(3 Punkte)

1. Write a graphical viewer for Game of Life using the Pygame library
   (pygame.org).  As an example of how to use the library, we added the file
   ``pygame_demo.py``. 

2. Write a function that does the reverse of the ``lifestring`` function, taking
   a string as an argument and turning it into a set of life cells. There are
   tests for this in ``blatt4.py``.

3. Combine the two above into a commandline program that takes a file containing
   the description of the initial configuration of the board and runs it with
   the pygame viewer. There is an example file ``factory.life``.


