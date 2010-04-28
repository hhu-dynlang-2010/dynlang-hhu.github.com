>>> class A(type):
...     def f(self):
...          print "hello"
...                       
>>> class MyType(type):
...     def f(self):
...          print "hello"
...                       
>>> A = None
>>> MyType.__base__
<type 'type'>      
>>> class A(object):
...     __metaclass__ = MyType
...     def g(self):
...          print "bye"
...                     
>>> a = A()             
>>> a.g()               
bye                     
>>> a.f()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'A' object has no attribute 'f'
>>> A.f()                                      
hello                                          
>>> class K(object):
...     pass        
...                 
>>> K.mro()         
[<class '__main__.K'>, <type 'object'>]
>>> a.mro()                            
Traceback (most recent call last):     
  File "<stdin>", line 1, in <module>  
AttributeError: 'A' object has no attribute 'mro'
>>> A.mro()                                     
[<class '__main__.A'>, <type 'object'>]         
>>> bool.mro()                                  
[<type 'bool'>, <type 'int'>, <type 'object'>]  
>>> class A(object):                            
...     pass                                    
...                                             
>>> class B(object):                            
...     pass                                    
...                                             
>>> B.__base__
<type 'object'>
>>> B.__base__ = A
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: readonly attribute        
>>> B.__bases__ = (A, )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __bases__ assignment: 'A' deallocator differs from 'object'
>>> class A(object):                                                  
...     pass                                                          
...                                                                   
>>> class B(A):
...     pass   
...            
>>> class C(A):
...     pass   
...            
>>> C.__bases__ = (B, )
>>>                    
>>>                    
>>> class Meta(type):
...     def __init__(self, class B(A):
  File "<stdin>", line 2              
    def __init__(self, class B(A):    
                           ^          
SyntaxError: invalid syntax           
>>> ...     pass                      
  File "<stdin>", line 1              
    ...     pass                      
    ^                                 
SyntaxError: invalid syntax           
>>>                                   
>>>                                   
>>>                                   
>>>                                   
>>>                                   
>>> class Meta(type):
...     def __init__(self, class B(A):
  File "<stdin>", line 2              
    def __init__(self, class B(A):    
                           ^          
SyntaxError: invalid syntax           
>>>     def __init__(self, class B(A):
  File "<stdin>", line 1              
    def __init__(self, class B(A):    
    ^                                 
IndentationError: unexpected indent   
>>>                                   
>>>                                   
>>>                                   
>>>                                   
>>>                                   
>>>                                   
>>>                                   
>>>                                   
>>>                                   
>>>                                   
>>> class Meta(type):
...     def __init__(self, name, bases, dct):
...          print "creating class", name, "with base", bases[0]
...          dct["hello"] = 1                                   
...          type.__init__(self, name, bases, dct)
...                                               
>>> class B(object):                              
...                                               
  File "<stdin>", line 2                          

    ^
IndentationError: expected an indented block
>>>
>>> class B(object):
...     __metaclass__ = Meta
...
creating class B with base <type 'object'>
>>>
>>>
>>> class A(object):
...     pass
...
>>> class A(object):
...     a = 1
...
>>> class B(object):
...     a = 2
...
>>> a = A()
>>> a.__class__
<class '__main__.A'>
>>> a.__class__ = B
>>> a.a
2
>>>
>>>
>>>
>>>
>>> #______________________________________________________
>>>
>>> class A(object):
...     def f(self, x):
...         self.x = x
...
>>> a = A()
>>> m = a.f
>>> m
<bound method A.f of <__main__.A object at 0x9b5a9ec>>
>>> m(4)
>>> a.x
4
>>> m(7)
>>> a.x
7
>>> a1 = A()
>>> m1 = a1.f
>>> M = A.f
>>> M(a1, 6)
>>> a1.x
6
>>> a.f(5)
>>>
>>>
>>> #______________________________________________________
>>>
>>>
>>> class A(object):
...     def __getattr__(self, attrname):
...         return attrname             
...                                     
>>> a = A()
>>> a.abc  
'abc'      
>>> a.hello_world
'hello_world'    
>>>
