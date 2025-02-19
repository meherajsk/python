
#object = property and methods
#a class is a blueprint for creating objects or object constructors
#objects are instances of classes

class myclass:
    x = 5

print(myclass)
p1 = myclass()
print(p1.x)


"""
__init__() function is always executed at the time of object creation.
is used to assingn values to objects' properties.
"""

print()
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("meheraj", 24)
print(p1.name)
print(p1.age)


"""__str__() function is used to return a string representation of the object.
"""

#The string representation of an object WITHOUT the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)



#The string representation of an object WITH the __str__() function:
print()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)


#Insert a function that prints a greeting, and execute it on the p1 object:
print()
class person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunction(self):
    print("Hello my name is " + self.name + " and I am " + str(self.age))

    
p1 = person("meheraj", 24)
p1.myfunction()

p1.age = 49
p1.myfunction()

del p1.age
#del p1
#p1.myfunction() #error

del p1
#p1.myfunction() #error

"""class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
"""

class person:
  pass
p2 = person