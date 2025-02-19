class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printname(self):
        print("hello my name is " + self.name)

x = person("meheraj", 24)
x.printname()  

'''
# a child class derived from the person class
class student(person):
    pass
# creating an object from student class
y = student("mehraj", 24)
y.printname()




class student(person):
    def __init__(self, name, age):# we have added __init__() , the child class will no longer inherit the parent's __init__() function
        person.__init__(self, name, age) # to keep the inheritance of the parent's __init__() , add a call to the parent's __init__().
        
        
z = student("afroz", 23)
z.printname() # hello my name is afroz

'''
# by super function
class student(person):
    def __init__(self, name, age):
        super().__init__(name, age)
    
f = student("meheaj", 23)
f.printname()




# add properties
class student(person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduation_year = year

    def detail(self):
        print(f"name:{self.name}\nage:{str(self.age)}\ngraduation year:{str(self.graduation_year)}")


c = student("mehraj", 23, 2022)
c.printname()
print(c.graduation_year)
print()
c.detail()







