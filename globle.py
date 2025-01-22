x = "awesome"

def myfun():
    print("python " + x)

myfun()



def myfun2():
    x = "fantastic"
    print("python is " + x)

myfun2()
print("python is " + x)


def myfun3():
    global x
    x = "global"

myfun3()

print(x)










