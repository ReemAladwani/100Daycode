Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> age = 36
>>> txt = "My name is Jhon, I am " + age
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    txt = "My name is Jhon, I am " + age
TypeError: Can't convert 'int' object to str implicitly
>>> txt = "My name is Jhon, and I am {}"
>>> print(txt.format(age))
My name is Jhon, and I am 36
>>> quantity = 3
>>> itemno = 567
>>> price = 49.95
>>> myorder = "I want {} pieces of item {} for {} dollars."
>>> print(myorder.format(quantity,itemno,price))
I want 3 pieces of item 567 for 49.95 dollars.
>>> myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
>>> print(myorder.format(quantity,itemno,price))
I want to pay 49.95 dollars for 3 pieces of item 567.
>>> 
