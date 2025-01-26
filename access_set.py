thisset = {"apple", "bananah", "cherry"}

for x in thisset:
    print(x)

print("banana" in thisset)
print("orange" not in thisset)

thisset.add("orange")
print(thisset)


thisset2 = {"meheraj", "amirul", "mominur"}
thisset.update(thisset2)
print(thisset)

