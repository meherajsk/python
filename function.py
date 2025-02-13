def my_function(name):
    """
    Prints a greeting with the given name.

    Parameters:
    name (str): The name to be included in the greeting.

    Returns:
    None
    """
    print("my name is",name)

my_function("meheraj")


def my_function(fname, lname):
    print(fname+" "+ lname)

my_function("sk", "meheraj")

#my_function("meheraj") error because it has 2 argument but we have put 1

print()
def my_function(*kids):
    print("the youngest kid is ", kids[-1])

my_function("meheraj", "amirul", "mominur", "mijanul", "sohel")

#arguments with key
def my_funcion(kid1, kid2, kid3):
    print("the youngest kid is " + kid3)

my_funcion(kid1 = "mominur", kid2 = "meheraj", kid3 = "sohel")



#kwargs 
def my_function(**kid):
    print("his last name is " + kid["lname"] + " and his age is " + str(kid["age"]))

my_function(fname = "meheraj", lname = "sk" , age = 24)



#default parameter value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


#passing a list as an argumentdef my_function(food):

def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)



#return value
print("\nTo let a function return a value, use the return statement:")
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


"""
function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
"""
def myfunction():
  pass

#positional only argument
'''
You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
To specify that a function can have only positional arguments, add , / after the arguments:
'''

def my_function(x, /):
  print(x)

my_function(3)

#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
def my_function(x):
  print(x)

my_function(x = 3)

"""
But when adding the , / you will get an error if you try to send a keyword argument:
"""
def my_function(x, /):
  print(x)

#my_function(x = 3)

"""
To specify that a function can have only keyword arguments, add *, before the arguments:
"""

def my_function(*, x):
  print(x)

my_function(x = 3)



"""
Combine Positional-Only and Keyword-Only
"""

"""
You can combine the two argument types in the same function.
Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
"""

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)




"""Recursion"""

"""
Python also accepts function recursion, which means a defined function can call itself.
Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
"""

print()
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)