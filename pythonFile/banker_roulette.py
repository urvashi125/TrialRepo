import random
name_string = input("give me everybody's names , sperated by comma . \n")
# name_string="Urvashi, Sanjeev, Neha, Surbhi"
names = name_string.split(", ")
# print(len(names))
number = random.randint(1, len(names)-1)

print(names[number] + " is going to pay" )
