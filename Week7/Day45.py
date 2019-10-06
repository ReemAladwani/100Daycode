Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> mytuple = ("apple","banana","cherry")
>>> myit = iter(mytuple)
>>> print(next(myit))
apple
>>> print(next(myit))
banana
>>> print(next(myit))
cherry
>>> mystr = "banana"
>>> myit = iter(mystr)
>>> print(next(myit))
b
>>> print(next(myit))
a
>>> print(next(myit))
n
>>> print(next(myit))
a
>>> print(next(myit))
n
>>> print(myit))
SyntaxError: unmatched ')'
>>> print(next(myit))
a
>>> mytuple=("apple","banana","cherry")
>>> for x in mytuple:
	print(x)

	
apple
banana
cherry
>>> class MyNumbers:
	def __iter__(self):
		self.a = 1
		return self

	
>>> def __next__(self):
	x = self.a
	self.a +=1
	return x

>>> myclass = MyNumbers()
>>> myiter = iter(myclass)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    myiter = iter(myclass)
TypeError: iter() returned non-iterator of type 'MyNumbers'
>>> myclass = MyNumbers()
>>> myiter = iter(myclass)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    myiter = iter(myclass)
TypeError: iter() returned non-iterator of type 'MyNumbers'
>>> class mynumbers:
	def __iter__(self):
		self.a = 1
		return self

	
>>>  class mynumbers:
	 
SyntaxError: unexpected indent
>>> class mynumbers:
	def __iter__(self):
		self.a = 1
		return self
	def __next__(self):
		x = self.a
		self.a +=1
		return x

	
>>> myclass = mynumbers()
>>> myiter = iter(myclass)
>>> print(next(myiter))
1
>>> print(next(myiter))
2
>>> print(next(myiter))
3
>>> print(next(myiter))
4
>>> print(next(myiter))
5
>>> class mynumbers:
	def __iter__(self):
		self.a =1
		return self
	def __next__(self):
		if self.a<=20:
			x = self.a
			self.a+=1
			return x
		else:
			raise StopIteration

		
>>> myclass = mynumbers()
>>> myiter = iter(myclass)
>>> for x in myiter:
	print(x)

	
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
>>> 
