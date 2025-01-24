this_list = ["apple" , "mango", "banana", "orange"]
for x in this_list:
    print(x,)

print("\nBy index value")
for i in range(len(this_list)):
    print(this_list[i])


#using a while loop
i = 0
while i < len(this_list):
    print(this_list[i])
    i = i + 1

#short hand forloop
#will prit all item
[print(y) for y in this_list]

for y in ["apple", "banana", "coco", "light"]:
    print(y)

#list comprehension
fruit = ["apple", "banana", "kiwi", "mango"]
new_list = []
for x in fruit:
    if "a" in x:
        new_list.append(x)
print(new_list)

#anotherway 
new_list_1 = [x for x in fruit if "a" in x]
print(new_list_1)

# new_list = [expression for item iterable if condition ==true]
#the condition like a filter that only accept the item that evaluate to true

new_list_2 = [x for x in fruit if x != "apple"]
print(new_list_2)

#whit no if statement
newlist = [x for x in fruit]
print(newlist)

newlist1 = [x for x in range(10)]
print(newlist1)

newlist3 = [x.upper() for x in fruit ]
print(newlist3)

#you can set the outcome to whatever you like
newlist4 =['hello' for x in fruit]
print(newlist4)

#the expression also can contain conditions
newlist5 = [x if x != "banana" else "orange" for x in fruit]
print(newlist5)

