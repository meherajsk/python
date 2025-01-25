thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() #alphanumarially, ascending, by default
print(thislist)

thislist = [12, 23, 0, 9, 7, 45,98,74,]
thislist.sort()
print(thislist)

thislist.sort(reverse = True)
print(thislist)
#You can also customize your own function by using the keyword argument key = function.

#The function will return a number that will be used to sort the list (the lowest number first):
def myfun(n):
    return abs(n-50)

thislist.sort(key = myfun)
print(thislist)

thislist1 = ["meheraj", "amirul", "Mominur", "Bijanur"]

thislist1.sort(key = str.lower) #case insensetive
print(thislist1)

thislist1.reverse()
print(thislist1) #reverrse the current sorting orderof element

mylist = thislist.copy()
print(mylist) #make a copy of alist whith the copy() method
#another way 
mylist1 = list(mylist)
print(mylist1)

#by slice operator
mylist2 = mylist[:]
print(mylist2)

mylist3 = mylist1 + mylist2
print(mylist3)

#another way 
for x in mylist1:
    mylist2.append(x)

print(mylist2)

#extend method
mylist1.extend(mylist2)
print(mylist1)

x = mylist1.count(0)
print(x)







