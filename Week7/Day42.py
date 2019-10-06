Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class person:
	def __init__(self, name,age):
		self.name = name
		self.age =age
	def myfunc(self):
		print("Hello my name is "+self.name)

		
>>> p1 = person("Jhon",36)
>>> p1.myfunc()
Hello my name is Jhon
>>> class person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def myfunc(self):
		print("hello ny name is "+ self.name)

		
>>> p1 = person("Jhon",36)
>>> p1.age = 40
>>> print(p1.age)
40
>>> class person:
	def __init__(self,name,age):
		self.name =name
		self.age =age
	def myfunc(self):
		print("Hello my name is "+ self.name)

		
>>> p1 = person("Jhon",36)
>>> del p1.age
>>> print(p1.age)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(p1.age)
AttributeError: 'person' object has no attribute 'age'
>>> del p1
>>> peint(p1)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    peint(p1)
NameError: name 'peint' is not defined
>>> 
