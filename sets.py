#store multiple items in a single variable
#unordered and unindexed. No duplicate members. unchangeable but can remove and add items

thisset = {"apple", "banana", "cherry"}
print(thisset) # {'banana', 'apple', 'cherry'} cause unordered

#cant cahnge items but can add items or remove items

thisset = {"apple", "banana", "cherry", "apple"}    
print(thisset) # {'banana', 'apple', 'cherry'} cause no duplicate members  

thisset1 = {"apple", "banana", "cherry", 1, 2, True, False, 0}
print(thisset1) # True and 1 and 0 and False are considered as same 


print(len(thisset1)) 

#can be any data typea and can be mixed data types
#set is an object with data type set
#set() constructor to make a set

myset = set(("apple", "banana", "cherry"))
print(myset) # {'banana', 'apple', 'cherry'} cause unordered