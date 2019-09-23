Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def my_function():
	print("Hello from a function")

	
>>> my_function()
Hello from a function
>>> def my_function(fname):
	print(fname + "Refsnes")

	
>>> my_function("Email")
EmailRefsnes
>>> def my_function(fname)
SyntaxError: invalid syntax
>>> def my_function(fname):
	print(fname + " Refsnes")

	
>>> my_function("Email")
Email Refsnes
>>> my_function("Tobias")
Tobias Refsnes
>>> my_function("Linus")
Linus Refsnes
>>> def my_function(country = "Norway"):
	print("I am from " + country)

	
>>> my_function("sweden")
I am from sweden
>>> my_function("India")
I am from India
>>> my_function
<function my_function at 0x10e9da9d0>
>>> my_function()
I am from Norway
>>> my_function("Brazil")
I am from Brazil
>>> 
