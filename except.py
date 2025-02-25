'''the try block lets you test a block of code for errors'''
#x = 5
try:
    print(x)
except:
    print("An exception occurred")


print()
#x = 5
try:
    print(x)
except NameError: # Print one message if the try block raises a NameError and another for other errors:
    print("Variable x is not defined")
except:
    print("An exception occurred")


print()
#x = 5
try:
    print("hello")
except:
    print("something else went wrong")
else: # else executed if no errors were raised:
    print("Nothing went wrong")


print()
try:
    print(x)
except:
    print("something went wrong")
finally:
    print("The 'try except' is finished")
# The finally block, if specified, will be executed regardless if the try block raises an error or not.





print()
#The try block will raise an error when trying to write to a read-only file:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  
# The program can continue, without leaving the file object open




"""
As a Python developer you can choose to throw an exception if a condition occurs.
To throw (or raise) an exception, use the raise keyword.
"""


#Raise an error and stop the program if x is lower than 0:

x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")


y = "hello"

if not type(y) is int:
  raise TypeError("Only integers are allowed")