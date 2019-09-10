Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> thislist = ['apple','banana','cherry']
>>> print(len(thislist))
3
>>> thislist.append('orange')
>>> print(thislist)
['apple', 'banana', 'cherry', 'orange']
>>> del thislist[3]
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> thislist.insert(1,'orange')
>>> print(thislist)
['apple', 'orange', 'banana', 'cherry']
>>> thislist.remove("banana")
>>> print(thislist)
['apple', 'orange', 'cherry']
>>> thislist.pop()
'cherry'
>>> print(thislist)
['apple', 'orange']
>>> thislist.append('cherry')
>>> print(thislist)
['apple', 'orange', 'cherry']
>>> thislist.pop(0)
'apple'
>>> print(thislist)
['orange', 'cherry']
>>> thislist.clear()
>>> print(thislist)
[]
>>> thislist = ['apple','banana','cherry']
>>> mylist = thislist.copy()
>>> print(mylist)
['apple', 'banana', 'cherry']
>>> thislist.pop(0)
'apple'
>>> print(thislist)
['banana', 'cherry']
>>> print(mylist)
['apple', 'banana', 'cherry']
>>> thislist = mylist
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> thislist.pop(0)
'apple'
>>> print(mylist)
['banana', 'cherry']
>>> print(thislist)
['banana', 'cherry']
>>> thislist.insert(0,'apple')
>>> mylist= list(thislist)
>>> print(mylist)
['apple', 'banana', 'cherry']
>>> thislist = list(('apple','banana','cherry'))
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> thislist.count()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    thislist.count()
TypeError: count() takes exactly one argument (0 given)
>>> x = thislist.count()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    x = thislist.count()
TypeError: count() takes exactly one argument (0 given)
>>> x = thislist.count("cherry")
>>> print(x)
1
>>> print (thislist)
['apple', 'banana', 'cherry']
>>> index = thislist.index("banana")
>>> print(index)
1
>>> thislist1 = ["A","B","C"]
>>> thislist.extend(thislist1)
>>> print(thislist)
['apple', 'banana', 'cherry', 'A', 'B', 'C']
>>> thislist.reverse()
>>> print(thislist)
['C', 'B', 'A', 'cherry', 'banana', 'apple']
>>> thislist.sort()
>>> print(thislist)
['A', 'B', 'C', 'apple', 'banana', 'cherry']
>>> thislist.count("A")
1
>>> thislist.insert(2,"A")
>>> print(thislist)
['A', 'B', 'A', 'C', 'apple', 'banana', 'cherry']
>>> thislist.count("A")
2
>>> 
