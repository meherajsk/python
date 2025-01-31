#set1 = {"a", "b", "c", "d"}
#set2 = {1, 2, 3, 4}

#set3 = set1.union(set2)
#set3 = set1 | set2   another way to add two sets
#print(set3)

set4 ={"meheraj", "amirul", "flowerr"}

#myset = set1 | set2 | set4
#print(myset)
#union allows us to add different typea
mytuple = ("meheraj1", "amirul1", "flower1")

#z = myset.union(mytuple)
#print(z)

#the | operator only allows us to join sets however union allows us to join different types

#set1.update(set4)
#print(set1)

#both uion and update exclude any duplicate value

set1 = {"apple", "banana", "cherry"}
set2 = {"goole", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#can use & same result

set3 = set1 & set2
print(set3)

#& only allows you to jion set not other data type like an intersection()

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)
print(set1)

#INTERSECTION_UPDATE() method will keep only the items that are present in both sets

set1 = {"apple", "banana", "cherry", 0 , True, 2, 1}
set2 = {False, "google", 1, "apple", 2}

set3 = set1.intersection(set2)
print(set3)

#intersection() method will return a new set, that only contains the items that are present in both sets

set1 = {"apple", "banana", "cherry", 0 , True, 2, 1}
set2 = {False, "google", 1, "apple", 2}

set3 = set1.difference(set2)
print(set3)

# - can do the same but cant do with other data types

set1 = {"apple", "banana", "cherry", 0 , True, 2, 1}
set2 = {False, "google", 1, "apple", 2}

set3 = set1 - set2
print(set3)

#the difference_update() method will also keep the items from 1st set thst are not in the other set , but it will change the original set intead of returnion a new set.
set1 = {"apple", "banana", "cherry", 0 , True, 2, 1}
set2 = {False, "google", 1, "apple", 2} 
set1.difference_update(set1)
print(set1)


set3 = set1.symmetric_difference(set2)
print(set3)
#also can use ^ but cant use with other data types

set1.symmetric_difference_update(set2)
print(set1)



