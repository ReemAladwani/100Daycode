Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = []
>>> print(s)
[]
>>> numbers = [1,2,3,4,5]
>>> print(numbers)
[1, 2, 3, 4, 5]
>>> thislist = ["apple", "banana","cherry"]
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> thislist = ["apple","banana","cherry",1,2,3]
>>> print(thislist)
['apple', 'banana', 'cherry', 1, 2, 3]
>>> flonubers = [1.6,9.8,4.5,3.1]
>>> print(flonumbers)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(flonumbers)
NameError: name 'flonumbers' is not defined
>>> print(flonubers)
[1.6, 9.8, 4.5, 3.1]
>>> thislist = ["apple","banana","cherry"]
>>> print(thislist[1])
banana
>>> for x in thislist:
	print(x)

	
apple
banana
cherry
>>> thislist[1] = "blackcurrant"
>>> print(thislist)
['apple', 'blackcurrant', 'cherry']
>>> del thislist[0]
>>> print(thislist)
['blackcurrant', 'cherry']
>>> del thislist
>>> print(thislist)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(thislist)
NameError: name 'thislist' is not defined
>>> thislist = ["A","B","C","D","E"]
>>> del thislist[0]
>>> print(thislist)
['B', 'C', 'D', 'E']
>>> del thislist[1]
>>> print(thislist)
['B', 'D', 'E']
>>> 
