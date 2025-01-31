from change_items_dictionary import thisdict
for x in thisdict:
    print(x)

print()
# printing value
for x in thisdict:
    print(thisdict[x])

print()
for x in thisdict.values():
    print(x)

print()
# loop through key and value
for x, y in thisdict.items():
    print(x,"   ",y)
