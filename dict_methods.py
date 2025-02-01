#fromkeys()
#dict.fromkeys(keys, value)
#
#Parameter	Description
#keys	Required. An iterable specifying the keys of the new dictionary
#value	Optional. The value for all keys. Default value is None

x = ('key1', 'key2', 'key3')
y =0
thisdict = dict.fromkeys(x , y)
print(thisdict)

x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)

#dictionary.get(keyname, value)
#
#Parameter	Description
#keyname	Required. The keyname of the item you want to return the value from
#value	Optional. A value to return if the specified key does not exist.
#Default value None

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("price", 15000)

print(x)


#pop()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")

print(car)

#dictionary.pop(keyname, defaultvalue)
#keyname	Required. The keyname of the item you want to remove
#defaultvalue	Optional. A value to return if the specified key do not exist.

#If this parameter is not specified, and the no item with the specified key is found, an error is raised
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.pop("model")

print(x)


#setdefault()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)



#dictionary.setdefault(keyname, value)

#keyname	Required. The keyname of the item you want to return the value from
#value	Optional.
#If the key exist, this parameter has no effect.
#If the key does not exist, this value becomes the key's value
#Default value None



car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print(x)

#update()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"mj":"white"})

print(car)
