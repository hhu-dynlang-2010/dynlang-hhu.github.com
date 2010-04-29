=======================================
Dynamic Languages - Übungen Blatt 4
=======================================

:Abgabedatum: 27. November 2008
:Subversion URL: svn://wyvern.cs.uni-duesseldorf.de/dynlang08


Aufgabe 1 - Pygame
------------------

1. Write a graphical viewer for Game of Life using the Pygame library
   (pygame.org).  As an example of how to use the library, we added the file
   ``pygame_demo.py``. 

2. Write a function that does the reverse of the ``lifestring`` function, taking
   a string as an argument and turning it into a set of life cells. There are
   tests for this in ``blatt4.py``.

3. Combine the two above into a commandline program that takes a file containing
   the description of the initial configuration of the board and runs it with
   the pygame viewer. There is an example file ``factory.life``.


Aufgabe 2 - Prototypes
----------------------

The point of this exercise is to explore a different approach to object-oriented
programming, called prototype-based programming. In prototype-based programming
there is no distinction at all between classes and objects. The task of this
exercise is to implemented a class ``ProtoObject`` in Python whose instances
behave like prototype-objects. This behaviour includes:

 - Every prototype-object has a number of attributes. Among those attributes
   there is a special attribute called ``parent`` which must be another
   prototype-object or ``None``.

 - When trying to read an attribute from a prototype-object, first the
   attributes of the object itself are checked, then the attributes of the
   ``parent`` object, and so on.

 - When reading an attribute, and that attribute's value has a ``__get__``
   method, that method should be called to get proper binding behaviour.

 - Writing an attribute works different from Python: When writing an attribute
   the ``parent`` chain is searched for a place where the attribute already
   exists. The new value is put into this prototype-object. When the attribute
   exists nowhere yet, it is put into the original object.

 - If the ``parent`` attribute is not specified, it is set to a base
   prototype-object called ``default_parent``.

 - The ``default_parent`` object has just one attribute, a method ``clone`` that
   can be used to make a copy of a prototype-object.


In addition to ``ProtoObject`` implement a metaclass ``ProtoMeta`` that can be
used to build prototype-objects using the class-syntax. ProtoMeta needs to
implement ``__call__`` and ``__call__`` should return a new instance of
``ProtoObject``.

The file ``blatt4.py`` contains a number of tests for prototype-objects. If you
hit under-specified behaviour during the implementation, decide on a sensible
behaviour and write a test for it.
