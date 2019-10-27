import re
txt = "The rain in Spain"
#x = re.search("^The.*Spain$", txt)
x = re.search("\AThe",txt)


if (x):
    print("YES! We have a match!")
else:
    print("No match")
