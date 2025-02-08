fruit = ["apple", "banana", "cherry", "kiwi"]
for x in fruit:
    print(x)

print()
for x in "banana":
    print(x)

print()
for x in fruit:
    print(x)
    if x == "banana":
        break

#exit the loop when x is banana
print()
for x in fruit:
    if x == "banana":
        break
    print(x)


print()
for x in fruit:
    if x == "banana":
        continue
    print(x)

#range()
print()
for x in range(4):
    print(x)


print()
for x in range(2, 4):
    print(x)


print()
for x in range(2, 30, 3):
    print(x)


print()
print("a block of code to be executed when the loop is finished")
for x in range(9):
    print(x)
else:
    print("finished")



print()
print("The else block will NOT be executed if the loop is stopped by a break statement")
for x in range(9):
    if x == 7: break
        #pass
    print(x)
else:
    print("finished")


print()
print("Print each adjective for every fruit:")
adj = ["red", "healthy", "big", "tasty"]
for x in adj:
    for y in fruit:
        print(x, y)
    print()
        


#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass
