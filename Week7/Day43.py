Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class person:
	def __init__(self,fname,lname):
		self.firstname =fname
		self.lastname=lname
	def printname(self):
		print(self.firstname,self.lastname)

		
>>> x = person("Jhon","Doe")
>>> x.printname()
Jhon Doe
>>> class person:
	def __init__(self,fname,lname):
		self.firstname =fname
		self.lastname =lname
	def printname(self):
		print(self.firstname,self.lastname)

		
>>> class student(person):
	pass

>>> x = student("Mike","Olsen")
>>> x.printnmae()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    x.printnmae()
AttributeError: 'student' object has no attribute 'printnmae'
>>> x.printname()
Mike Olsen
>>> class student(person):
	def __init__(self,fname,lname):
		person.__init__(self,fname,lname)

		
>>> x = student("Mike","Olsen")
>>> x.printname()
Mike Olsen
>>> 
