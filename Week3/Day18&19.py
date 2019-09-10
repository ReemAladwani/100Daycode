Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruits = ['apple','banana','cherry']
>>> fruits.append('orange')
>>> print(fruits)
['apple', 'banana', 'cherry', 'orange']
>>> fruits.count('banana')
1
>>> fruits.pop(2)
'cherry'
>>> print(fruits)
['apple', 'banana', 'orange']
>>> fruits.insert(0,'cherry')
>>> print(fruits)
['cherry', 'apple', 'banana', 'orange']
>>> fruits.reverse()
>>> print(frutis)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(frutis)
NameError: name 'frutis' is not defined
>>> print(fruits)
['orange', 'banana', 'apple', 'cherry']
>>> fruits.sort()
>>> print(fruits)
['apple', 'banana', 'cherry', 'orange']
>>> tuple = ('java','python','swift')
>>> if 'python' in tuple:
	print("Yes, 'python' is in the programming language tuple")

	
Yes, 'python' is in the programming language tuple
>>> 
