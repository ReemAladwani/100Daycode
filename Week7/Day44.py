Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class person:
	def __init__(self,fname,lname):
		self.firstname=fname
		self.lastname=lname
	def printname(self):
		print(self.firstnmae,self.lastname)

		
>>> class student(person):
	def __init__(self,fname,lname):
		super().__init__(fname,lname)

		
>>> x = student("Mike","Olsen")
>>> x.printname()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x.printname()
  File "<pyshell#6>", line 6, in printname
    print(self.firstnmae,self.lastname)
AttributeError: 'student' object has no attribute 'firstnmae'
>>> class person:
	def __init__(self,fname,lname):
		self.firstname=fname
		self.lastname=lname
	def printname(self):
		print(self.firstname,self.lastname)

		
>>> class student(person):
	def __init__(self,fname,lname):
		super().__init__(fname,lname)

		
>>> x = student("Mike","Olsen")
>>> x.printname()
Mike Olsen
>>> class student(person):
	def __init__(self,fname,lname):
		super().__init__(fname,lname)
		self.graduationyear = 2019

		
>>> x =student("Mike","Olsen")
>>> print(x.graduationyear)
2019
>>> class student(person):
	def __init__(self,fname,lname,year):
		super().__init__(fname,lname)
		self.graduationyear = year

		
>>> x = student("Mike","Olsen",2019)
>>> print(x.graduationyear)
2019
>>> class student(person):
	def __init__(self,fname,lname,year):
		super().__init__(fname,lname)
		self.graduationyear = year
	def welcome(self):
		print("Welcome" ,self.firstname,self.lastname,"to the class of ",self.graduationyear)

		
>>> x = student("Mike","Olsen",2019)
>>> x.welcome()
Welcome Mike Olsen to the class of  2019
>>> 
