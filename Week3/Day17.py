Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> thistuple = ('apple','banana','cherry')
>>> if 'apple' in thistuple:
	print("Yes, 'apple' is in the fruits tuple")

	
Yes, 'apple' is in the fruits tuple
>>> thistuple = ("بايثون",)*3
>>> print(thistuple)
('بايثون', 'بايثون', 'بايثون')
>>> thistuple = ("بايثون")*3
>>> print(thistuple)
بايثونبايثونبايثون
>>> thistuple1 = (1,2,3,4)
>>> thistuple2 = (5,6)
>>> thistuple3 = thistuple1 + thistuple2
>>> print(thistuple3)
(1, 2, 3, 4, 5, 6)
>>> x = (3,4,5,6)
>>> x = x + (1,2,3)
>>> print(x)
(3, 4, 5, 6, 1, 2, 3)
>>> print(len(x))
7
>>> thistuple = tuple(('apple','banana','cherry'))
>>> print(thistuple)
('apple', 'banana', 'cherry')
>>> print(len(thistuple))
3
>>> thislist = [3,4,5,6,"A","B"]
>>> thistuple = tuple(thislist)
>>> print(thistuple)
(3, 4, 5, 6, 'A', 'B')
>>> thistuple.count("A")
1
>>> thistuple.index("4")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    thistuple.index("4")
ValueError: tuple.index(x): x not in tuple
>>> thistuple.index(4)
1
>>> 
