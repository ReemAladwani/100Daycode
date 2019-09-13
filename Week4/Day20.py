Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> thisset = {}
>>> print (thisset)
{}
>>> thisset = {'apple','banana','cherry'}
>>> print(thisset)
{'banana', 'cherry', 'apple'}
>>> thisset = {'Ahmad','Ahmad',1,2,1,5}
>>> print(thisset)
{1, 2, 5, 'Ahmad'}
>>> thisset = {'apple','banana','cherry'}
>>> for x in thisset:
	print(x)

	
banana
cherry
apple
>>> print('banana' in thisset)
True
>>> thisset.add('orange')
>>> print(thisset)
{'orange', 'banana', 'cherry', 'apple'}
>>> thisset.update(["mango","grapes"])
>>> print(thisset)
{'grapes', 'cherry', 'apple', 'mango', 'banana', 'orange'}
>>> 
