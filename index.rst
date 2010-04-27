================================
   Dynamic Languages SS 2010
================================



Die Vorlesung findet mittwochs um 11-13 Uhr in Raum 25.12.02.33 statt. 

.. Am 26.05.2010 findet die Vorlesung in Raum 25.12.02.55 statt. 

Es gibt zwei Übungstermine, Mittwoch 09-11 und 16-18. Die Übung findet im
Seminarraum 25.12.02.55 statt. Bitte Laptops mitbringen!

Material
==================

14.4.2010: Introduction to Dynamic Languages and Python
-------------------------------------------------------

- Slides about Organization__
- Slides for `Lecture 1`__
- `console session`__
- `Demo program`__ (`.py Datei`__)
- Useful links: `Python Tutorial`__; `py.test`__

.. __: organization.pdf
.. __: l1.pdf
.. __: console1.html
.. __: l1.html
.. __: l1.py
.. __: http://docs.python.org/tutorial/
.. __: http://codespeak.net/py/dist/test.html


21.4.2010: Single-Inheritance Object-Orientation
--------------------------------------------------

- `Demo program`__ with ``remove_duplicates`` and ``memo_maker`` (`.py Datei`__).
- Slides for `Lecture 2`__
- `Demo program`__, implementing ``myisinstance``, ``myissubtype`` and ``send`` (`.py Datei`__).
- `Introduction to mercurial and py.test`__
- Slides about `Exercises`__
- Useful link: `Python Types and Objects`__

.. __: l2.html
.. __: l2.py
.. __: l2.pdf
.. __: l2_class.html
.. __: l2_class.py
.. __: tools.pdf
.. __: exercise.pdf
.. __: http://www.cafepy.com/article/python_types_and_objects/contents.html


Übungsblätter
=============

Blatt 1
--------

- `Blatt 1`__, bis zum 26. April 2010.
- dazugehörige `Test-Datei`__

.. __: aufgaben/blatt1.pdf
.. __: aufgaben/blatt1.py

Blatt 2
--------

- `Blatt 2`__, bis zum 3. Mai 2010.
- dazugehörige `Test-Datei`__, sowie `Test-Daten`__

.. __: aufgaben/blatt2.pdf
.. __: aufgaben/blatt2.py
.. __: aufgaben/faust_1

.. raw:: html

    <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/de/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/3.0/de/88x31.png" /></a><br />Unless stated otherwise, the material for the lecture by Carl Friedrich Bolz, Armin Rigo, David Schneider and is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/de/">Creative Commons Attribution-Noncommercial-Share Alike 3.0 Germany License</a>.

..
    31.10.08: Python's Object Model
    -------------------------------

    * `Demo program`__ demonstrating changing the class of an object
    * `Demo program`__ implementing approximations to ``getattr`` and ``setattr`` in
      pure Python
    * `Python documentation`__ about special methods
    * Second part of Python Types and Objects: `Python Attributes and Methods`__
    * Paper__ describing the base model of ``type`` and ``object``.

    .. __: l3.html
    .. __: l3_getattr.html
    .. __: http://docs.python.org/reference/datamodel.html#special-method-names
    .. __: http://www.cafepy.com/article/python_attributes_and_methods/contents.html
    .. __: http://portal.acm.org/citation.cfm?id=38822

    7.11.08: Python's Object Model: Special Methods and Applications
    ----------------------------------------------------------------

    * `Demo program`__ for creating a ``Singleton`` metaclass
    * `Demo program`__ for overriding indexing to implement a spreadsheet
    * `Demo program`__ for a simple vector class
    * `Demo program`__ for a lazily computed attribute
    * `Python Documentation`__ describing ``__get__`` and ``__set__``

    .. __: l4_singleton.html
    .. __: l4_spreadsheet.html
    .. __: l4_vector.html
    .. __: l4_lazyattr.html
    .. __: http://docs.python.org/reference/datamodel.html#implementing-descriptors

    14.11.08: ``__get__`` Special method and Duck Typing
    ----------------------------------------------------

    * `Console session`__ for using the ``__get__`` special method
    * `Duck Typing`__ Wikipedia article

    .. __: l5_get_session.pycon.html
    .. __: http://en.wikipedia.org/wiki/Duck_typing

    21.11.08: Generators and Coroutines
    -----------------------------------

    * `Documentation about generators`__
    * `Demo program`__ with various simple generators
    * `greenlet documentation`__
    * Wikipedia article about `coroutines`__

    .. __: http://www.python.org/doc/2.2.2/whatsnew/node5.html
    .. __: l6_generators.html
    .. __: http://codespeak.net/py/dist/greenlet.html
    .. __: http://en.wikipedia.org/wiki/Coroutines

    28.11.08 Prototype-based Object-Orientation
    -------------------------------------------

    * `pygame example`__ using generators

    * Slides for `Lecture 7`__
    * `Demo program`__ using prototypes
    * One of the early `papers`__ proposing the use of prototypes

    .. __: l7_pygame.html
    .. __: l7.html
    .. __: l7_point.py
    .. __: http://web.media.mit.edu/~lieber/Lieberary/OOP/Delegation/Delegation.html

    5.12.08 Multiple Inheritance
    ----------------------------

    * Slides for `Lecture 8`__
    * `Demo program`__ using multiple inheritance to do multimethods 
    * `Paper`__ describing C3, the algorithm used in Python to do superclass linearization

    .. __: l8.html
    .. __: l8_pairtype.html
    .. __: http://192.220.96.201/dylan/linearization-oopsla96.html

    12.12.08 Smalltalk
    ----------------------------

    * Slides for `Lecture 9`__
    * "Squeak by Example" book__
    * `Example images`__ used in the lecture

    .. __: smalltalk-slides.pdf
    .. __: http://squeakbyexample.org/
    .. __: http://codespeak.net/~cfbolz/squeak-example-images.tar.gz

    19.12.08 Wiederholung
    -----------------------

    * Slides for `Lecture 10`__

    .. __: l10.html

    9.01.09 Implementation of Dynamic Languages
    ---------------------------------------------

    * Slides for `Lecture 11`__

    .. __: l11.html

    16.01.09 Implementation of Dynamic Languages: Object Models
    ------------------------------------------------------------

    * Slides for `Lecture 12`__

    .. __: l12.html

    23.01.09 PyPy's Approach to VM Implementation
    ------------------------------------------------------------

    * Slides for `Lecture 13`__

    .. __: l13.pdf

    30.01.09 An Introduction to Partial Evaluation
    -----------------------------------------------

    * Slides for `Lecture 14`__

    .. __: l14.pdf

    6.02.09 Rückblick
    ------------------

    * Slides for `Lecture 15`__

    .. __: l15.html

    Übungsblätter
    =============

    * `Blatt 1`__, `(pdf)`__ bis zum 6. November 2008
    * `Blatt 2`__, `(pdf)`__ bis zum 13. November 2008
    * `Blatt 3`__, `(pdf)`__ bis zum 20. November 2008
    * `Blatt 4`__, `(pdf)`__ bis zum 27. November 2008
    * `Blatt 5`__, `(pdf)`__ bis zum 4. Dezember 2008
    * `Blatt 6`__, `(pdf)`__ bis zum 11. Dezember 2008
    * `Blatt 7`__, `(pdf)`__ bis zum 18. Dezember 2008
    * `Blatt 8`__, `(pdf)`__ bis zum 8. Januar 2009
    * `Blatt 9`__, `(pdf)`__ bis zum 15. Januar 2009
    * `Blatt 10`__, `(pdf)`__ bis zum 29. Januar 2009


    .. __: aufgaben/blatt1.html
    .. __: aufgaben/blatt1.pdf
    .. __: aufgaben/blatt2.html
    .. __: aufgaben/blatt2.pdf
    .. __: aufgaben/blatt3.html
    .. __: aufgaben/blatt3.pdf
    .. __: aufgaben/blatt4.html
    .. __: aufgaben/blatt4.pdf
    .. __: aufgaben/blatt5.html
    .. __: aufgaben/blatt5.pdf
    .. __: aufgaben/blatt6.html
    .. __: aufgaben/blatt6.pdf
    .. __: aufgaben/blatt7.html
    .. __: aufgaben/blatt7.pdf
    .. __: aufgaben/blatt8.html
    .. __: aufgaben/blatt8.pdf
    .. __: aufgaben/blatt9.html
    .. __: aufgaben/blatt9.pdf
    .. __: aufgaben/blatt10.html
    .. __: aufgaben/blatt10.pdf
