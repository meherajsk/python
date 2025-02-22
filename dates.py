import datetime as dt

x = dt.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

# creating a date time module from datetime class
y = dt.datetime(2020, 5, 17) #timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).
print(y)

# strftime() method
print(y.strftime("%B"))
print(y.strftime("%A"))
print(y.strftime("%w"))
print(y.strftime("%d"))
print(y.strftime("%b"))
print(y.strftime("%m"))
print(y.strftime("%y"))
print(y.strftime("%Y"))
print(y.strftime("%H"))
print(y.strftime("%I"))
print(y.strftime("%p"))
print(y.strftime("%M"))
print(y.strftime("%S"))
print(y.strftime("%f"))
print(y.strftime("%z"))
print(y.strftime("%Z"))
print(y.strftime("%Z"))
print(y.strftime("%W"))
print(y.strftime("%c"))
print(y.strftime("%C"))
print(y.strftime("%x"))
print(y.strftime("%X"))
print(y.strftime("%%"))
print(y.strftime("%G"))
print(y.strftime("%u"))
print(y.strftime("%V"))



