Python 3.8.0b3 (v3.8.0b3:4336222407, Jul 29 2019, 09:46:03) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> cars = ["Ford","Volvo","BMW"]
>>> for x in cars:
	print(x)

	
Ford
Volvo
BMW
>>> cars.append("Honda")
>>> print(cars)
['Ford', 'Volvo', 'BMW', 'Honda']
>>> cars.pop(1)
'Volvo'
>>> print(cars)
['Ford', 'BMW', 'Honda']
>>> cars.remove("Honda")
>>> print(cars)
['Ford', 'BMW']
>>> 
