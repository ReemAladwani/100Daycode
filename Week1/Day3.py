Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 5
>>> y = "jhon"
>>> print(x)
5
>>> print(y)
jhon
>>> x = 4 #x is of type int
>>> x = "Sally" # x is now of type str
>>> print(x)
Sally
>>> x = "jhon"
>>> print(x)
jhon
>>> # double quotes are the same as single quotes:
>>> x = 'jhon'
>>> print(x)
jhon
>>> x, y , z ="orange", "Banana", "cherry"
>>> print(x)
orange
>>> print(y)
Banana
>>> print(z)
cherry
>>> x = y = z ="orange"
>>> print(x)
orange
>>> print(y)
orange
>>> print(z)
orange
>>> x = "awesome"
>>> print("python is " + x)
python is awesome
>>> x = "python is"
>>> y = "awesome"
>>> z = x + y
>>> print(z)
python isawesome
>>> x = "python is "
>>> print (z)
python isawesome
>>> z = x + y
>>> print(z)
python is awesome
>>> x = 5
>>> y = 10
>>> print(x + y)
15
>>> x = 5
>>> y = "jhon"
>>> print(x+y)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(x+y)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
