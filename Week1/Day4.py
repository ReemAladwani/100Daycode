Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 1 #int
>>> y = 2.8 #float
>>> z = 1j #complex
>>> print(type(x))
<class 'int'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'complex'>
>>> x = 1
>>> y = 23467895
>>> z = -6532
>>> print(type(x))
<class 'int'>
>>> print(type(y))
<class 'int'>
>>> print(type(z))
<class 'int'>
>>> x = 1.10
>>> y = 1.0
>>> z = -35.87
>>> print(type(x))
<class 'float'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'float'>
>>> x = 35e3
>>> y = 12E4
>>> z = -87.7e100
>>> print(type(x))
<class 'float'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'float'>
>>> x = 3+5j
>>> y = 5j
>>> z = -5j
>>> print(type(x))
<class 'complex'>
>>> print(type(y))
<class 'complex'>
>>> print(type(z))
<class 'complex'>
>>> x = 1
>>> y = 2.8 #float
>>> z = 1j #complex
>>> #convert from int to float
>>> a = float(x)
>>> #convert from float to int
>>> b = int(y)
>>> #convert from in to complex
>>> c = complex(x)
>>> print(a)
1.0
>>> print(type(a))
<class 'float'>
>>> print(b)
2
>>> print(type(b))
<class 'int'>
>>> print(c)
(1+0j)
>>> print(type(c))
<class 'complex'>
>>> import random
>>> print(random.randrange(1,10))
2
>>> print(random.randrange(1,10))
6
>>> print(random.randrange(1,10))
2
>>> 
