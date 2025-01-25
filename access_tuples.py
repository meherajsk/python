thistuple = ("apple", "mango", "banana", "orange", "kiwi")
print(thistuple[3])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

if "apple" in thistuple:
    print("yes available")

#you cant change the tuple value but you can by transforming it to a list then to tuple

thislist = list(thistuple)
thislist[1] = "kiwi"
thislist.append("flower")
thistuple = tuple(thislist)
print(thistuple)

#allowed to add tuple to tuple

y = ("meheraj",)
thistuple += y
print(thistuple)

#as it is unchangeable so we cant remove items but can in same previous way

#del keyword can delete the tuple comletely
del thistuple
print(thistuple)