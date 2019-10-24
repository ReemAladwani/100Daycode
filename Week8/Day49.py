Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=300
>>> def myfunc():
	x = 200
	print(x)

	
>>> myfunc()
200
>>> print(x)
300
>>> def myfunc():
	global x
	x = 300

	
>>> myfunc()
>>> 
>>> print(x)
300
>>> def myfunc():
	x = 300

	
>>> myfunc()
>>> print(X)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined
>>> x = 300
>>> def myfunc():
	global x
	x = 200

	
>>> myfunc()
>>> print(x)
200
>>> 
