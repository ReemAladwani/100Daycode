Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = lambda a :a +10=
SyntaxError: invalid syntax
>>> x = lambda a : a + 10
>>> print(x(5))
15
>>> x = lambda a, b :a * b
>>> print(x(5, 6))
30
>>> x = lambda a, b, c : a+ b + c
>>> print(x(5,6,2))
13
>>> 
