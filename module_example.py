#from m_module import *
import m_module as m
import platform

m.greeting("Jonathan")

x = m.person1["age"]
print(x)

y = dir(m)
print(y)
x = platform.system()
print(x)

