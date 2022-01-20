import re
pattern ='^[A-Z]'
value = input("Enter your string : \n")

found = re.match(pattern,value)

if found:
    print("String started with capital letter")
else:
    print("Please give string which starts with capitol letter")