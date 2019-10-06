Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class myclass:
	x = 5

	
>>> print(myclass)
<class '__main__.myclass'>
>>> class myclass:
	x = 5

>>> p1 = myclass()
>>> print(p1.x)
5
>>> class person:
	def __init__(mysillyobject, name, age)
	
SyntaxError: invalid syntax
>>> def __init__(mysillyobject, name, age):
	mysillyobject.name = name
	mysillyobject.age = age

	
>>> def myfunc(abc):
	print("Hello my name is"+abc.name)

	
>>> p1 = person("Johon",36)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    p1 = person("Johon",36)
NameError: name 'person' is not defined
>>> class person:
	def __init__(mysillyobject, name, age):
		mysillyobject.name = name
		mysillyobject.age = age

		
>>> def mysunc(abc):
	print("Hello my name is" + abc.name)

	
>>> p1 = person("John",36)
>>> p1.myfunc()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    p1.myfunc()
AttributeError: 'person' object has no attribute 'myfunc'
>>> class person:
	def __init__(self,name,age):
		self.name = name
		self.age = age

		
>>> p1 = person("Jhon",36)
>>> print(p1.anme)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(p1.anme)
AttributeError: 'person' object has no attribute 'anme'
>>> print(p1.name)
Jhon
>>> print(p1.age)
36
>>> class person:
	def __init__(x,name,age):
		x.name = name
		x.age = age
	def myfunc(abc):
		print("hello my name is" + abc.name)

		
>>> p1 = person("Jhon",34)
>>> p1.myfunc()
hello my name isJhon
>>> 
