a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


#boolen
print(bool("hello"))
print(bool(15))

x = "hello"
y = 15

print(bool(x))
print(bool(y))

#to determine a certain data type
print(isinstance(y, int))
print(isinstance(x, int))

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


#functions can return a boolean value
class myclass():
    def __len__(self):
        return 0
    
myobj =myclass()

print(bool(myobj))
