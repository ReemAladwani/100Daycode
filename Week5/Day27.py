Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 33
>>> b = 200
>>> if b > a:
	print("b is greater than a")

	
b is greater than a
>>> if b > a:
print("b is greater than a")
SyntaxError: expected an indented block
>>> b = 33
>>> if b > a:
	print("b is greater than a")
     elif a == b:
	     
SyntaxError: unindent does not match any outer indentation level
>>> if b > a:
	print("b is greater than a")
elif a == b:
	print("a and b are equal")

	
a and b are equal
>>> a = 200
>>> if b > a:
	print("b is greater than a")
elif a == b:
	print("a and b are equal")
else:
	print("a is greater than b")

	
a is greater than b
>>> if b > a:
	print("b is greater than a")
else:
	print("b is not greater than a")

	
b is not greater than a
>>> if a > b: print("a is grater than b")

a is grater than b
>>> a = 2
>>> b = 330
>>> print("A") if a > b else print("B")
B
>>> a = 330
>>> print("A") if a > b else print("=") if a == b else print("B")
=
>>> 
>>> a = 200
>>> b = 33
>>> c = 500
>>> if a > b and c > a:
	print("Both conditions are True")

	
Both conditions are True
>>> if a > b or a > c:
	print("At least one of the conditions is True")

	
At least one of the conditions is True
>>> a = 41
>>> if x > 10:
	print("Above ten,")
if x > 20:
	
SyntaxError: invalid syntax
>>> if x > 10:
	print("Above ten,")
	if x > 20:
		print("and also above 20!")
		else:
			
SyntaxError: invalid syntax
>>> if x > 10:
	print("Above ten,")
	if x > 20:
		print("and also above 20!")
	else:
		print("but not above 20.")

		
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    if x > 10:
NameError: name 'x' is not defined
>>> x = 41
>>> if x > 10:
	print("Above ten,")
	if x> 20:
		print("and also above 20!")
	else:
		print("but not above 20.")

		
Above ten,
and also above 20!
>>> 
