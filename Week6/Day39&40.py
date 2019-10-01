Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def rec(power, num)
SyntaxError: invalid syntax
>>> def rec (power,num):
	if power < 1:
		return 1
	else:
		return num* rec(power -1 ,num)

	
>>> print(rec(3,5))
125
>>> list =[-4,-6,-5,-1,2,3,7,9,88]
>>> x = lambda 1s :1s if 1s > 0 else None
SyntaxError: invalid syntax
>>> 
>>> x = lambda ls :ls if ls > 0 else None
>>> for i in list:
	if x(i) != None:
		print(x(i))

		
2
3
7
9
88
>>> 
