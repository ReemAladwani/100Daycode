Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> thisdict = {
	"brand" : "Ford",
	"model" : "Mustang",
	"year" : 1964
	}
>>> if "model" in thisdict:
	print("Yes,'model' is one of the keys in the thisdict dictionary")

	
Yes,'model' is one of the keys in the thisdict dictionary
>>> print(len(thisdict))
3
>>> thisdict["color"] = "red"
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
>>> thisdict.pop("color")
'red'
>>> print(tgisdic)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(tgisdic)
NameError: name 'tgisdic' is not defined
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> thisdict.popitem()
('year', 1964)
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang'}
>>> thisdict["year"] = 1995
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1995}
>>> del thisdict["model"]
>>> print(thisdict)
{'brand': 'Ford', 'year': 1995}
>>> del thisdict
>>> print(thisdict)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(thisdict)
NameError: name 'thisdict' is not defined
>>> thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year":1964
	}
>>> thisdict.clear()
>>> print(thisdict)
{}
>>> 
