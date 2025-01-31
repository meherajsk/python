import change_items_dictionary
mj = change_items_dictionary.thisdict
print(mj)

mj.pop("model")
print(mj)

# popitem removes the last incerted item
mj.popitem()
print(mj)


# del removes the item with key value and whole directory
del mj["brand"]
print(mj)

#del mj
#print(mj) #show error


# empties directory
mj.clear()
print(mj)
