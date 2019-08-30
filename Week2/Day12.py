Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 5
>>> y = 7
>>> s = "Please, I want {} sandwishes and {} donutes"
>>> s = s.replace("I", "We")
>>> print(s)
Please, We want {} sandwishes and {} donutes
>>> print(s.format(x, y))
Please, We want 5 sandwishes and 7 donutes
>>> print(s.upper())
PLEASE, WE WANT {} SANDWISHES AND {} DONUTES
>>> 
