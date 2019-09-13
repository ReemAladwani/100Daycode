Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> thisdict = {}
>>> print(thisdict)
{}
>>> thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
	}
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> x = thisdict["model"]
>>> print(x)
Mustang
>>> x = thisdict.get("model")
>>> print(x)
Mustang
>>> thisdict["year"] = 2018
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
>>> for x in thisdict:
	print(x)

	
brand
model
year
>>> for x in thisdict:
	print(thisdict[x])

	
Ford
Mustang
2018
>>> for x in thisdict.values():
	print(X)

	
Traceback (most recent call last):
  File "<pyshell#23>", line 2, in <module>
    print(X)
NameError: name 'X' is not defined
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
>>> for x in thisdict.values():
	print(X)

	
Traceback (most recent call last):
  File "<pyshell#27>", line 2, in <module>
    print(X)
NameError: name 'X' is not defined
>>> print(thisdict.values())
dict_values(['Ford', 'Mustang', 2018])
>>> for x,y in thisdict.items():
	print(x, y)

	
brand Ford
model Mustang
year 2018
>>> print(thisdict.items())
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2018)])
>>> 
