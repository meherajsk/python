a = 1
b = 2
if b > a:
    print("b is greater than a")




if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")




if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")
else:
    print("b is greater than a")




#short hand if 
if a > b: print("a is greater than b")

#if else in one line
print("a is greater than b") if a > b else print("b is greater than a")


#if ifelse else in one line
print("a") if a > b else print("=") if a == b else print("b")


# combined operator by logical opeator
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# by "or"
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")



#not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")



#nested if
print()
x = 41
if x > 10:
    print("above ten")
    if x > 20:
      print("above 20")
    else:
      print("not above 20")


#pass
#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass