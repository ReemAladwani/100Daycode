Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def myfunc():
	x = 300
	print(x)

	
>>> myfunc()
300
>>> def myfunc():
	x = 300
	def myinnerfunc():
		print(x)

		
>>> myinnerfunc()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    myinnerfunc()
NameError: name 'myinnerfunc' is not defined
>>> myfunc()
>>> def myfunc():
	x = 300
	def myinnerfunc():
		print(x)
		myinnerfunc()

		
>>> myfunc()
>>> x = 300
>>> def myfunc():
	print(x)

	
>>> myfunc()
300
>>> print(x)
300
>>> 
