Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def myfunc(n):
	return lambda a: a*n

>>> mydoubler = myfunc(2)
>>> print(mydoubler(11))
22
>>> mytripler = myfunc(3)o
SyntaxError: invalid syntax
>>> mytripler = myfunc(3)
>>> print(mytripler(11))
33
>>> 
