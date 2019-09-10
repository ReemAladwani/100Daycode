Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> thislist = ["A","B","C","D","E"]
>>> print(thislist[1:3])
['B', 'C']
>>> print(thislis[0:4])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(thislis[0:4])
NameError: name 'thislis' is not defined
>>> print(thislist[0:4])
['A', 'B', 'C', 'D']
>>> print(thislist[2:4])
['C', 'D']
>>> print(thislist[0:2])
['A', 'B']
>>> thislist = ['apple','banana','cherry']
>>> if 'apple' in thislist:
	print("Yes, 'apple' is in the fruits list")

	
Yes, 'apple' is in the fruits list
>>> thislist = ["بايثون"]*4
>>> print(thislist)
['بايثون', 'بايثون', 'بايثون', 'بايثون']
>>> thislist1 = ['Ahmed','Khalid','Omar']
>>> thislist2 = ['Sara','Hind','Batool']
>>> thislist3 = thislist1 + thislist2
>>> print(thislist3)
['Ahmed', 'Khalid', 'Omar', 'Sara', 'Hind', 'Batool']
>>> 
