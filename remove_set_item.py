thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#thisset.remove("kiwi") #item does not exist then it will show error
#print(thisset)

thisset.add("banana")
print(thisset)

thisset.discard("banana")
print(thisset)
#if item doesnot exists then it will not show error

x = thisset.pop()#return value is removed item and it removes item randomly
print(x)
print(thisset)

thisset.clear()#empties set
print(thisset)

thisset = {"apple", "banana","cherry"}
del thisset
print(thisset)

