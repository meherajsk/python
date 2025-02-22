import re

"""Search the string to see if it starts with "The" and ends with "Spain":"""

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("YES! We have a match!") 
else:
    print("No match")



txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 



txt = "The rain in Spain"
x = re.split("\s", txt) # Split at each white-space character:
print(x)



txt = "The rain in Spain"
x = re.split("\s", txt, 1) #Split the string only at the first occurrence:
print(x)




txt = "The rain in Spain"
x = re.sub("\s", "9", txt) #Replace every white-space character with the number 9:
print(x)



txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)# Replace the first 2 occurrences:
print(x)



txt = "The    rain in Spain"
x = re.search("ai", txt) #Do a search that will return a Match Object:
print(x) #this will print an object