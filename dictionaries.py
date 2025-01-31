#ordered changeable does not allow dublicate values

thisdic = {
    "name": "Sk Meheraj Rahaman",
    "age": "23",
    "success": "no"
    
}

print(thisdic)
print(thisdic["age"])

#Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print(len(thisdic))

#can be any data type
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#From Python's perspective, dictionaries are defined as objects with the data type 'dict':
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

#It is also possible to use the dict() constructor to make a dictionary.
thisdic = dict(name = "meheraj", age =23, success = "no")
print(thisdic)