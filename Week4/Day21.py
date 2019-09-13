Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> thisset = {'apple','banana','cherry'}
>>> print(len(thisset))
3
>>> thisset.remove('banana')
>>> print(thisset)
{'cherry', 'apple'}
>>> thisset.remove('banana')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    thisset.remove('banana')
KeyError: 'banana'
>>> thisset.add('banana')
>>> print(thisset)
{'banana', 'cherry', 'apple'}
>>> thisset.discard('apple')
>>> print(thisset)
{'banana', 'cherry'}
>>> thisset.add('apple')
>>> x = thisset.pop()
>>> print(x)
banana
>>> print(thisset)
{'cherry', 'apple'}
>>> thisset.clear()
>>> print(thisset)
set()
>>> thisset.update(['apple','banana','cherry'])
>>> print(thisset)
{'banana', 'cherry', 'apple'}
>>> del thisset
>>> print(thisset)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(thisset)
NameError: name 'thisset' is not defined
>>> thisset = set(('apple','banana','cherry'))
>>> print(thisset)
{'banana', 'cherry', 'apple'}
>>> 
