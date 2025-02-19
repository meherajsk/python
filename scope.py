"""
Local Scope
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
"""


def myfunc():
  x = 300
  print(x)

myfunc()


"""The local variable can be accessed from a function within the function:"""
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


"""
Global Scope
A variable created in the main body of the Python code is a global variable and belongs to the global scope.
Global variables are available from within any scope, global and local.
"""

x = 300

def myfunc():
  print(x)

myfunc()

print(x)




"""
If you operate with the same variable name inside and outside of a function, 
Python will treat them as two separate variables, 
one available in the global scope (outside the function) and 
one available in the local scope (inside the function):
"""

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)


"""If you use the global keyword, the variable belongs to the global scope:"""
def myfunc():
  global x
  x = 300

myfunc()

print(x)



"""
To change the value of a global variable inside a function, 
refer to the variable by using the global keyword:
"""

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)



"""to acces outer function's variable in inner function"""
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())