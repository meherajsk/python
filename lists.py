thislist = ["apple", "banana", "cherry", "apple"]
print(thislist)

print(len(thislist))

list1 = ["abc", "true", 34, "male", 78]
print(list1)

#list conductor to create list list()
listdemo = list(("apple", "banana", " coco", "lemon"))
print(listdemo)
print(listdemo[-1])
print(listdemo[1:3])
print(listdemo[:3])
print(listdemo[2:])
print(listdemo[-3:-1])


if "mango" in listdemo:
    print("available")
else:
    print("not available")
    
#listdemo[1:3] = ["meheraj", "jemes"]
print(listdemo)

#listdemo[1:4] = ["meheraj"]
print(listdemo)

listdemo[1:2] =["meheraj", "meherajs wife"]
print(listdemo)


#insert items
listdemo.insert(2, "flower")
print(listdemo)

#append items
listdemo.append("orange")
print(listdemo)

#extend items
name = ["rahul", "sohana", "salim"]
listdemo.extend(name) #the element will be added at the end of the list
print(listdemo)

my_tuple = ("kiwi", "mango", "pineapple")
listdemo.extend(my_tuple)
print(listdemo)

#remove items

listdemo.remove("meheraj")
print(listdemo)

listdemo.append("apple")
listdemo.remove("apple")
print(listdemo) #it will remove the first occurance of the element


#pop() method removes the specified index, (or the last item if index is not specified)
listdemo.pop(4)
print(listdemo)

#del keyword removes the specified index
del listdemo[2]
print(listdemo)

#del listdemo
print(listdemo) #it will give an error because listdemo is deleted  by del keyword

listdemo.clear()
print(listdemo) #it will clear the list




