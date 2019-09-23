Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruits = ["apple","banana","cherry"]
>>> for x in fruits:
	print(x)

	
apple
banana
cherry
>>> for x in "banana":
	print(x)

	
b
a
n
a
n
a
>>> for x in fruits:
	print(x)
	if x == "banana":
		break

	
apple
banana
>>> for x in fruits:
	if x == "banana":
		break
	print(x)

	
apple
>>> for x in fruits:
	if x == "banana":
		continue
	print(x)

	
apple
cherry
>>> 
