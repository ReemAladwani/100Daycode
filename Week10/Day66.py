quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars"
print(myorder.format(quantity,itemno,price))

age = 36
name = "Jhon"
txt = "His name is {1}. {1} is {0} years old"
print(txt.format(age,name))
x = "I have a {carname}, it is a {model}"
print(x.format(carname="Ford",model = "Mustang"))