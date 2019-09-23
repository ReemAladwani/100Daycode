Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> for x in range(6):
	print(x)

	
0
1
2
3
4
5
>>> for x in range(2, 6):
	print(x)

	
2
3
4
5
>>> for x in range(2, 30,3):
	print(x)

	
2
5
8
11
14
17
20
23
26
29
>>> for x in range(6):
	print(x)
else:
	print("Finally finishing!")

	
0
1
2
3
4
5
Finally finishing!
>>> adj = ["red","big","tasty"]
>>> fruits = ["apple","banana","cherry"]
>>> for x in adj:
	for y in fruits:
		print(x,y)

		
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
>>> 
