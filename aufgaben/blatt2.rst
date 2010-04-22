=======================================
Dynamic Languages - Übungen Blatt 2
=======================================

:Abgabedatum: ``3. Mai 2010``


Aufgabe 1
---------
(2 Punkte)

1. Write a function that takes a string and computes a nested dictionary from it.
   The goal is to find out which words follow another word in this string.
   The dictionaries keys are therefore the words appearing in the string. The
   values are again dictionaries that map the following word to a number of
   occurrences. The test function is given in ``aufgaben/blatt1.py``.

2. Such a dictionary can be used to produce a random text that is similar to the
   text the dictionary was created from. To do this, start with a random word
   from the dictionary. Then pick a random word out of the words that followed
   the first word in the original text, with probabilities according to their
   occurrences.


Aufgabe 2
---------
(3 Punkte)

Change ``mygettattr`` from last lecture to add a way to add "virtual"
attributes to types without changing the type itself, which are only seen
when using ``mygettattr``.  These overrides can be added with a helper
functions. The test functions are given in ``aufgaben/blatt2.py``. 

Aufgabe 3
---------
(3 Punkte)



Aufgabe 4
---------
(2 Punkte)

A possible implementation of the forward part of the Burrows-Wheeler
transformation (Aufgabe 4 Blatt 1) is given in ``blatt2.py``. However, it has
the disadvantage that it builds in memory all shifted versions of the input
string, which uses memory that is O(n**2) where n is the length of the input
string. The point of this exercise is to rewrite this function to use memory
that is only linear in the input string length.  This can be done by writing a
class whose instances have a references to the original string and an shift
number that indicates how much the string is shifted. The class needs a __lt__
method that does comparisons between such instances correctly. Write tests that
test the behaviour of this class.  In addition, the existing tests for the
forward transformation should still pass.

