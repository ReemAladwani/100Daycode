Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def my_function(food):
	for x in food:
		print(x)

		
>>> fruits = ["apple","banana","cherry"]
>>> my_function(fruits)
apple
banana
cherry
>>> def my_function(x):
	return 5*x

>>> print(my_function(3))
15
>>> print(my_function(5))
25
>>> print(my_function(9))
45
>>> def my_function(child3,child2,child1):
	print("The youngest child is " + child3)

	
>>> my_function(child1= "Emil",child2 = "Tobias",child3 = "Linus")
The youngest child is Linus
>>> def my_function(*kids):
	print("The youngest child is "+ kids[2])

	
>>> my_function("Emil","Tobias","Linus")
The youngest child is Linus
>>> def tri_recursion(k):
	if(k>0):
		result = k+tri_recursion(k-1)
		print(result)
	else:
		result = 0
		return result

	
>>> print("\n\nRecursion Example Results")


Recursion Example Results
>>> tri_recursion(6)
1
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    tri_recursion(6)
  File "<pyshell#27>", line 3, in tri_recursion
    result = k+tri_recursion(k-1)
  File "<pyshell#27>", line 3, in tri_recursion
    result = k+tri_recursion(k-1)
  File "<pyshell#27>", line 3, in tri_recursion
    result = k+tri_recursion(k-1)
  [Previous line repeated 2 more times]
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
>>> tri_recursion(8)
1
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    tri_recursion(8)
  File "<pyshell#27>", line 3, in tri_recursion
    result = k+tri_recursion(k-1)
  File "<pyshell#27>", line 3, in tri_recursion
    result = k+tri_recursion(k-1)
  File "<pyshell#27>", line 3, in tri_recursion
    result = k+tri_recursion(k-1)
  [Previous line repeated 4 more times]
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
>>> 
