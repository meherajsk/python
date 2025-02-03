#Get the value of the "model" key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#There is also a method called get() that will give you the same result:
x = thisdict.get("year")
print(x)

#The keys() method will return a list of all the keys in the dictionary.

x = thisdict.keys()
print(x)


car = {
    "brand": "ford",
    "model": "Mustang",
    "year" : 1964
}

x = car.keys()

print(x)

car["color"] = "white"
print(x)


#The values() method will return a list of all the values in the dictionary.

x = car.values()
print(x)

car["year"] = 2023
print(x)
car["color"] = "red"
print(x)


# the item() method will return each item in a directory, as tuples in a list
x = thisdict.items()
print(x)

# if we change the main dictionary then it will be reflected in everywhere

# checking keys by "in"
if "model" in thisdict:
  print("yes it is present in thisdict variable")


