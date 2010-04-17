===================================
Dynamic Languages - Übungen Blatt 1
===================================

:Abgabedatum: 26. April 2010, 23:59:59 Uhr


Aufgabe 0
---------

(2 Punkte)

1. Install Python, easy_install, mercurial and py.test.

2. Make an account at bitbucket.org.

3. Build teams of two people and create one repository per team at bitbucket.
   Add the team members, ``cfbolz`` and ``bivab`` as writers.

4. Send David ``david.schneider@uni-duesseldorf.de`` an e-Mail with the names of the team
   members, the Matrikelnummern and bitbucket user names.


Aufgabe 1
---------

(2 Punkte)

Write a function that counts the number of lines and the number of words
in a file.  A word is any non-empty sequence of characters between
whitespace (as per the ``split()`` method of strings).  The test function
is given in ``aufgaben/blatt1.py``.


Aufgabe 2
---------

(2 Punkte)

1. The goal is to find a zero (in the mathematical sense) of some
   continuous function ``f(x)`` that takes and returns a real number
   (i.e. a float).  To do that, write a function ``find_zero(f, a, b)``
   that takes such a function ``f`` as argument, together with two floats
   ``a`` and ``b`` that give the bounds of the interval in which to
   search.  The ``find_zero`` function should check that ``f(a) < 0`` and
   ``f(b) > 0`` (or the other way around), and divide the interval in
   half, and repeats until the zero has been found with sufficient
   precision (e.g. at least 0.0001).  See the test in
   ``aufgaben/blatt1.py``.

2. Use the function from 1. to implement ``approximate_sqrt``. See the test in 
   ``aufgaben/blatt1.py``.

3. Write a function that takes an arithmetic expression as a string and
   turns it into a function, with one argument ``x``, that can be used in
   part 1.  See the test in ``aufgaben/blatt1.py``.  Hint: use the
   built-in ``eval()`` (type ``help(eval)`` in an interactive prompt).

4. Combine 1. and 3. in the obvious way.


Aufgabe 3
---------

(2 Punkte)

Change the function ``send(obj, message, *args)`` from the lecture
(http://wyvern.cs.uni-duesseldorf.de/hhu-dynlang/l2_class.py) to behave
differently when the message name is not found: instead of immediately
raising an ``AttributeError`` exception, it should try to send to the
same object a new message called ``"message_not_understood"``.  The
first argument of this new message should be the original string from
``message``.  The remaining arguments should be ``*args``, i.e. the
arguments of the original message.

If the ``"message_not_understood"`` message is not found, then ``send``
should raise ``AttributeError`` as before.

Start from the test in ``aufgaben/blatt1.py`` but write more tests.


Aufgabe 4
---------

(2 Punkte)

1. Implement the Burrows Wheeler transformation.  Start from the test in
   ``aufgaben/blatt1.py``.

2. Write your own test for the reverse transformation and implement it.

Reference: http://de.wikipedia.org/wiki/Burrows-Wheeler-Transformation

Please don't use the solution given on the English Wikipedia page (it is not very good).
