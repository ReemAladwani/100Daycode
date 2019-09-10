Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> thistuple = ("apple","banana","cherry")
>>> print(thistuple)
('apple', 'banana', 'cherry')
>>> thistuple = ()
>>> print(thistuple)
()
>>> thistuple = (3,)
>>> print(thistuple)
(3,)
>>> thistuple = (3,1.3,4.1,7)
>>> print(thistuple)
(3, 1.3, 4.1, 7)
>>> thistuple = ('Ahmed',1.4,4,"بايثون")
>>> print(thistuple)
('Ahmed', 1.4, 4, 'بايثون')
>>> print(thistuple[1])
1.4
>>> for x in thistuple:
	print(x)

	
Ahmed
1.4
4
بايثون
>>> thistuple[3] = 'orange'
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    thistuple[3] = 'orange'
TypeError: 'tuple' object does not support item assignment
>>> del thistuple
>>> print(thistuple)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(thistuple)
NameError: name 'thistuple' is not defined
>>> thistuple = ('apple','banana','cherry','orange')
>>> print(thistuple[0:3])
('apple', 'banana', 'cherry')
>>> 
