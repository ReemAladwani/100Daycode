import re
str = "The rain in Spain"
#x = re.sub("\s", "9",str)
#x = re.sub("\s", "9",str,2)
#x = re.search("ai",str)
x = re.search(r"\bS\w+",str)
print(x.span())
print(x.string)
print(x.group())