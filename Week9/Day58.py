import re
str = "The rain in Spain"
#x = re.findall("ai", str)

"""x =re.findall("portugal",str)
print(x)
if (x):
    print("Yes, there is at least one match!")
else:
    print("No match")
"""
#x = re.search("\s",str)
#print("The first white-space character is located: ",x.start())
#x=re.search("portugal",str)
x = re.split("\s",str)
print(x)