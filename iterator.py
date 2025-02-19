class myNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = myNumber()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


class alter:
    def __init__(self):
        self.a = 1
    
    def next_alt(self):
        x = self.a
        self.a += 1
        return x

myclass = alter()


print()
print(myclass.next_alt())
print(myclass.next_alt())
print(myclass.next_alt())
print(myclass.next_alt())
print(myclass.next_alt())
print(myclass.next_alt())
print(myclass.next_alt())
print(myclass.next_alt())
print(myclass.next_alt())
print(myclass.next_alt())
print(myclass.next_alt())
print(myclass.next_alt())
print(myclass.next_alt())
print(myclass.next_alt())



#stopIteration
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
        raise StopIteration
      

myclass = MyNumbers()
20
myiter = iter(myclass)

for x in myiter:
  print(x)