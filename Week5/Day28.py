Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> i = 1
>>> while i < 6:
	print(i)
	i += 1

	
1
2
3
4
5
>>> i= 1
>>> while i < 6:
	print(i)
	if i == 3:
		break
	i += 1

	
1
2
3
>>> i = 0
>>> while i < 6:
	i += 1
	if i == 3:
		continue
	print(i)

	
1
2
4
5
6
>>> i = 1
>>> while i < 6:
	print(i)
	i += 1
	else:
		
SyntaxError: invalid syntax
>>> i = 1
>>> while i< 6:
	print(i)
	i += 1
else:
	print("i is no longer less than 6")

	
1
2
3
4
5
i is no longer less than 6
>>> i = 10
>>> while i < 6:
	print(i)
	i += 1
else:
	print("i is no longer less than 6")

	
i is no longer less than 6
>>> 
