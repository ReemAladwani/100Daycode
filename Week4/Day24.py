Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> thisdict = {
	"brand": "Ford"
	"model": "Mustang"
	
SyntaxError: invalid syntax
>>> thisdict = {
	"brand":"Ford",
	"model":"Mustang",
	"year":1964
	}
>>> mydict = thisdict.copy()
>>> print(mydict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> mydict = dict(thisdict)
>>> print(mydict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> myfamily = {
	"child1" : {
		"name" :"Emil",
		"year" : 2004
		},
	"child2" : {
		"name": "Tobias",
		"year" :2007
		},
	"child3" :{
		"name" : "Linus",
		"year" : 2011
		}
	}
>>> print(myfamily)
{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
>>> child1 = {
	"name" : "Emil",
	"year" = 2004
	
SyntaxError: invalid syntax
>>> child1 = {
	"name": "Emil",
	"year":2004
	}
>>> child2 = {
	"nmae":"Tobias",
	"year" :2007
	}
>>> child3 = {
	"name":"Linus",
	"year": 2011
	}
>>> myfamily1 = {
	"child1" : child1,
	"child2" : child2,
	"child3" : child3
	}
>>> print(myfamily1)
{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'nmae': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
>>> thisdict = dict(brand = "Ford",model="Mustang","year" = 1964)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> thisdict = dict(brand ="Ford",model="Mustang",year=1964)
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> 
