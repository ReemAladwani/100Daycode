Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> numset = {1,3,5,7,8}
>>> numset.update([4,8,12])
>>> print(numset)
{1, 3, 4, 5, 7, 8, 12}
>>> numset.remove(8)
>>> print(numset)
{1, 3, 4, 5, 7, 12}
>>> numset.clear()
>>> print(numset)
set()
>>> thisdict = {
	"name":"pigeon",
	"type":"bird",
	"skin cover" :"feathers"
	}
>>> x = thisdict["type"]
>>> print(x)
bird
>>> thisdict["skin cover"] = "fur"
>>> print(thisdict)
{'name': 'pigeon', 'type': 'bird', 'skin cover': 'fur'}
>>> 
