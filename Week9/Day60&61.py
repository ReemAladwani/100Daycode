import  json
import re

tuple1=("Saturday","Sunday","Monday","Tuesday","wednesday","Thursday","Friday")
x = json.dumps(tuple1)
print(x)
str = "data is the new oil"
x1 = re.search(r"\bd\w+",str)
print(x1.group())



