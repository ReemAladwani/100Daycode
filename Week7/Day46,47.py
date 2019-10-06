Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Library:
	def __init__(x,book,shelf)
	
SyntaxError: invalid syntax
>>> class Library:
	def __init__(x,book,shelf):
		x.book = 300
		x.shelf = 45
	def print(x):
		print(x.book,x.shelf)

		
>>> class science_section(Library):
	def __init__(x,book,shelf,name):
		super().__init__(book,shelf)
		x.physicsbooks = name

		
>>> y = science_section(300 , 45, "physics1")
>>> print(y.physicsbooks)
physics1
>>> y = science_section(20,4,"physics1")
>>> print(y)
<__main__.science_section object at 0x10a47f1f0>
>>> print(y.book,y.shelf,y.physicsbooks)
300 45 physics1
>>> class science_section(Library):
	def __init__(x,book,shelf,name):
		super().__init__(book,shelf)
		x.book = 20
		x.shelf = 4
		x.physicsbooks = name

		
>>> y = science_section(20,4,"physics1")
>>> print(y.book,y.shelf,y.physicsbooks)
20 4 physics1
>>> 
